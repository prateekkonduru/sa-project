# sa-project

## Project Title: 
Success Academy Devops Project

## Project Description:

A vendor needs to upload a file to an S3 bucket every day for reporting purposes.  We want to make sure this bucket is emptied out on a weekly basis on Sunday's in order to keep costs down.  Please create an S3 bucket and Lambda function using Terraform and any other services you deem required to complete this task.   This process must be 100% automated and the Lambda function must be created using the latest version of Python.  We also would like the Python script to detect if there are any lingering files left over in the S3 bucket after being emptied and alert members of the DevOps team if any are found.
 
The candidate will Terraform the creation of AWS resources to help solve this problem.  The candidate will also be expected to provide an output file as well as a tfvars file.  We expect all modules and resources created to use variables as that is best practice in Terraform.  The Terraform will be tested by our team to make sure it applies and deploys properly.  Please provide a link to the repo this code is stored in, we will not accept a zip file.
 
## How it works

### Deploying Infrastructure 

1. Setup AWS Profile 
```
$ export AWS_ACCESS_KEY_ID="anaccesskey"
$ export AWS_SECRET_ACCESS_KEY="asecretkey"
$ export AWS_REGION="us-west-2"
```
3. Initiate Terraform 
```
terraform init
```
4. Plan terraform 
```
terraform plan
```
5. Apply terraform 
```
terraform apply
```

Additional Requirements for Email Notification:

In the lambda function please enter SNS_ARN and AWS_ACCESS_KEY_ID="anaccesskey",AWS_SECRET_ACCESS_KEY="asecretkey", AWS_REGION="us-west-2" in env variables of the configuration tab