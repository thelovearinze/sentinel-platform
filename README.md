# Sentinel Platform

Self-service Internal Developer Platform — Python-powered CLI that lets developers provision production-ready AWS environments (VPC and related resources) in minutes, without tickets or manual operations.

## Features

- **Self-service CLI**: Simple, guided workflow instead of Jira tickets or copy-paste scripts

- **Automated IaC Generation**: Generates clean Terraform code from Jinja2 templates and standardized blueprints

- **Zero-touch provisioning**: Automatically runs `terraform plan` and `terraform apply`

- **Post-deployment validation**: Confirms that provisioned resources reach the expected operational state

## Requirements

- Python 3.10 or higher
- Terraform ≥ 1.5 (installed globally)
- AWS credentials with permissions to create VPCs and related resources (`ec2:CreateVpc`, etc.)

## Quick Start

1. **Clone the repository and enter the directory**

   ```bash
   git clone https://github.com/thelovearinze/sentinel-platform.git
   cd sentinel-platform

2. **Create and activate a virtual environment**

   ````bash
    python3 -m venv venv
    source venv/bin/activate    # Linux / macOS


4. **Install dependencies**
   
   ````bash
      pip install -r requirements.txt

3. **Set required environment variables**

     ````bash
    export OPENAI_API_KEY="sk-..."
    export AWS_ACCESS_KEY_ID="AKIA..."
    export AWS_SECRET_ACCESS_KEY="..."
    export AWS_REGION="eu-west-1" # or your preferred region


Provision your first environment

    python portal.py provision
    

Example Output

Received Platform Request for: Sentinel-CRM
1. Generating Infrastructure Blueprint
2. Initializing Platform Engine
3. Validating Configuration (Plan)
4. Provisioning Resources (Apply)
SUCCESS: Project 'Sentinel-CRM' is live.

Testing

Run the unit tests (no AWS credentials required):

     
          python test_platform.py

Error Handling
- If Terraform fails to apply (e.g., quota limits), the deployer captures the stderr logs and reports the specific AWS error code.

- If the resource is created but does not reach an "Available" state, the Monitor flags the deployment as a FAILURE despite the Terraform success code.

