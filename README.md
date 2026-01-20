# Sentinel Platform: Internal Developer Portal

A Python-based self-service internal developer platform that automates the provisioning of AWS infrastructure. It runs as a CLI tool that allows developers to request production-ready environments without manual operational work.

## Features
- Self-Service CLI: Developers request infrastructure using a simple command-line interface.
- Automated IaC Generation: Generates Terraform code dynamically using Jinja2 templates and standardized blueprints.
- Zero-Touch Provisioning: Runs Terraform plan and apply automatically to provision AWS VPC infrastructure.
- SRE: Includes automated "Post-Deployment Health Checks" to verify Service Level Objectives  immediately after build.

## Requirements
- Python 3.10 
- Terraform installed globally
- AWS CLI credentials with permissions to create VPC resources

## Installation and Setup
Clone the repository:
git clone https://github.com/your-username/sentinel-platform.git
cd sentinel-platform

Set up a virtual environment:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Configure credentials:
OPENAI_API_KEY=your_key_here
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_REGION=your region

## Usage
python portal.py provision

Example output:
Received Platform Request for: Sentinel-CRM
--- [Step 1] Generating Infrastructure Blueprint ---
--- [Step 2] Initializing Platform Engine ---
--- [Step 3] Validating Configuration (Plan) ---
Do you want to apply this configuration to AWS Production? [Y/n]: y
--- [Step 4] Provisioning Resources (Apply) ---
SUCCESS: Project 'Sentinel-CRM' is live.

## Testing
python test_platform.py

## Error Handling
Infrastructure Failures: If Terraform fails during apply, for example due to quota limits, the platform captures and reports the specific AWS error returned by Terraform.
Post-Provisioning Failures: If resources are created but do not reach the expected state, the deployment is marked as failed even if Terraform exits successfully.
