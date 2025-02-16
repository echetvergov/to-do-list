FROM public.ecr.aws/lambda/python:3.12
WORKDIR /app

ARG DEBIAN_FRONTEND=noninteractive

# Install FastAPI and Mangum into the Lambda task root directory
RUN pip3 install fastapi --target "${LAMBDA_TASK_ROOT}"
RUN pip3 install mangum --target "${LAMBDA_TASK_ROOT}"
RUN pip3 install boto3 --target "${LAMBDA_TASK_ROOT}"
RUN pip3 install pyjwt requests --target "${LAMBDA_TASK_ROOT}"

# Copy the application code to the Lambda task root directory
COPY lambda.py ${LAMBDA_TASK_ROOT}/lambda.py

# Define the Lambda function handler
CMD [ "lambda.handler" ]
