A Python-based self-service internal developer platform that automates AWS infrastructure provisioning.
It runs as a CLI tool that lets developers request production-ready environments without manual operational work.

## Features

- **Self-Service CLI**
  Request infrastructure using a simple CLI workflow instead of tickets or ad-hoc scripts.

- **Automated IaC Generation**
  Generates Terraform code from Jinja2 templates and standardized blueprints.

- **Zero-Touch Provisioning**
  Runs `terraform plan` and `terraform apply` automatically to provision VPC infrastructure.

- **Post-Deployment Checks**
  Validates that provisioned resources reach the expected operational state after creation.

## Requirements

- Python 3.10
- Terraform installed globally
- AWS CLI credentials with permissions to create VPC resources

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sentinel-platform.git
cd sentinel-platform
2. Set up a Python virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Configure environment variables
export OPENAI_API_KEY="your_key_here"
export AWS_ACCESS_KEY_ID="your_aws_key"
export AWS_SECRET_ACCESS_KEY="your_aws_secret"
export AWS_REGION="eu-west-1"
Usage
Run the CLI to provision a new project:

python portal.py provision
Example Output
Received Platform Request for: Sentinel-CRM
1. Generating Infrastructure Blueprint
2. Initializing Platform Engine
3. Validating Configuration (Plan)
4. Provisioning Resources (Apply)
SUCCESS: Project 'Sentinel-CRM' is live.
Testing
Run unit tests locally without connecting to AWS:

python test_platform.py
Error Handling
Infrastructure failures
If Terraform fails during apply (for example due to quota limits), the platform captures and reports the specific error returned by Terraform.

Post-provisioning failures
If resources are created but do not reach the expected state, the deployment is marked as failed even if Terraform exits successfully.