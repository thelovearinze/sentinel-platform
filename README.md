# Sentinel Platform: Internal Developer Portal

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


  - 1. "Set up Python virtual environment"
    commands: |
      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt

  - 2.  "Configure environment variables"
    commands: |
      export OPENAI_API_KEY="sk-example-openai-key"
      export AWS_ACCESS_KEY_ID="AKIAEXAMPLE123456"
      export AWS_SECRET_ACCESS_KEY="exampleAwsSecretKeyValue123456"
      export AWS_REGION="eu-west-1"

usage:
  - description: "Provision a new environment using the CLI"
    commands: |
      python portal.py provision

example_output: |
  Received Platform Request for: Sentinel-CRM
  1. Generating Infrastructure Blueprint
  2. Initializing Platform Engine
  3. Validating Configuration (Plan)
  4. Provisioning Resources (Apply)
  SUCCESS: Project 'Sentinel-CRM' is live.

testing:
  - description: "Run unit tests locally without connecting to AWS"
    commands: |
      python test_platform.py

error_handling:
  - "Infrastructure failures: Terraform errors during apply (for example quota limits) are captured and reported."
  - "Post-provisioning failures: Resources that fail health or readiness checks mark the deployment as failed even if Terraform exits successfully."
