from aws_cdk import App, Stack
from constructs import Construct
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_dynamodb as dynamodb

class InfraProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # Define the DynamoDB table
        table = dynamodb.Table(
            self, "MyTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            ),
            table_name="MyDynamoDBTable"
        )

        # Create a Lambda function
        lambda_function = _lambda.Function(
            self, "MyFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Grant the Lambda function read/write permissions to the DynamoDB table
        table.grant_read_write_data(lambda_function)
