# app.py
from aws_cdk import App
from infra_project_stack import InfraProjectStack

app = App()
InfraProjectStack(app, "InfraProjectStack")
app.synth()
