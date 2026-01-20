# Sentinel Platform: Internal Developer Portal

Sentinel is a Python-based internal developer platform that automates AWS infrastructure provisioning. It runs as a CLI tool that allows engineers to request production-ready environments in a consistent and repeatable way, without manual operational intervention.

## Features
- **Self-Service Provisioning**  
  Engineers provision AWS infrastructure through a simple CLI workflow instead of manual tickets or ad-hoc scripts.

- **Standardized Infrastructure Blueprints**  
  Terraform configurations are generated dynamically using Jinja2 templates to enforce consistent network design and defaults.

- **Automated Provisioning Workflow**  
  Terraform plan and apply are executed automatically, reducing human error and speeding up environment creation.

- **Post-Provision Validation**  
  Deployed resources are checked to ensure they reach the expected operational state after creation.

## Requirements
- Python 3.10 or later
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
AWS_REGION=eu-west-1

## Usage

Run the CLI to provision a new project:
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

Run unit tests locally without connecting to AWS:
python test_platform.py

## Error Handling

Infrastructure Failures:  
If Terraform fails during apply, for example due to quota limits, Sentinel captures and reports the specific error returned by Terraform.

Post-Provisioning Failures:  
If resources are created but do not reach the expected state, the deployment is marked as failed even if Terraform exits successfully.
