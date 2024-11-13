from aws_cdk import App, Stack, CfnOutput
from constructs import Construct
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk.aws_lambda import FunctionUrlAuthType, HttpMethod

class InfraProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the DynamoDB table
        table = dynamodb.Table(
            self, "MyTable",
            partition_key=dynamodb.Attribute(
                name="task_id",
                type=dynamodb.AttributeType.STRING
            ),
            table_name="NewTable",
            time_to_live_attribute="ttl",
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        # Add the Global Secondary Index
        table.add_global_secondary_index(
            index_name="user-index",
            partition_key=dynamodb.Attribute(name="user_id", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="created_time", type=dynamodb.AttributeType.NUMBER),
            projection_type=dynamodb.ProjectionType.ALL
        )

        # Create a Lambda function
        lambda_function = _lambda.Function(
            self, "MyFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "TABLE_NAME": table.table_name
            }
        )

        # Grant the Lambda function read/write permissions to the DynamoDB table
        table.grant_read_write_data(lambda_function)

        # Add a function URL to the Lambda function
        function_url = lambda_function.add_function_url(
            auth_type=FunctionUrlAuthType.NONE,
            cors=_lambda.FunctionUrlCorsOptions(
                allowed_origins=["*"],
                allowed_methods=[HttpMethod.ALL],
                allowed_headers=["*"]
            )
        )

        # Output the function URL
        CfnOutput(self, "FunctionUrl", value=function_url.url)
