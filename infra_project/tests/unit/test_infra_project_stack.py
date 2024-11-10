import aws_cdk as core
import aws_cdk.assertions as assertions

from infra_project.infra_project_stack import InfraProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in infra_project/infra_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = InfraProjectStack(app, "infra-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
