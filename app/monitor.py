import boto3
import os
import sys
from dotenv import load_dotenv

load_dotenv()

def check_platform_health(project_name):
    """
    SRE Health Check: Verifies that the deployed infrastructure 
    is actually 'Available' in AWS.
    """
    region = os.getenv("AWS_REGION", "eu-west-1")
    ec2 = boto3.client('ec2', region_name=region)
    
    print(f"--- STARTING SRE HEALTH CHECK FOR '{project_name}' ---")
    
    # 1. Find the resource by the tags we assigned in the template
    try:
        response = ec2.describe_vpcs(
            Filters=[
                {'Name': 'tag:Name', 'Values': [f"{project_name}-vpc"]},
                {'Name': 'tag:ManagedBy', 'Values': ['Platform-Portal']}
            ]
        )
    except Exception as e:
        print(f"CRITICAL: Failed to connect to AWS API. Error: {e}")
        return False

    vpcs = response.get('Vpcs', [])
    
    # 2. Evaluate SLO (Service Level Objective)
    if not vpcs:
        print("SLO VIOLATION: Infrastructure was reported as 'Applied', but cannot be found in AWS.")
        return False
        
    target_vpc = vpcs[0]
    state = target_vpc['State']
    vpc_id = target_vpc['VpcId']
    
    if state == "available":
        print(f"SLO MET: Resource {vpc_id} is '{state}'.")
        print("--- HEALTH CHECK PASSED ---")
        return True
    else:
        print(f"SLO WARNING: Resource {vpc_id} is in state '{state}' (Expected: 'available').")
        return False

if __name__ == "__main__":
    # Check the specific project we just deployed
    check_platform_health("Lagos-Hub")