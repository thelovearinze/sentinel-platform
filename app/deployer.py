import subprocess
import os
import sys

def run_terraform_action(action="plan"):
    """
    Automates Terraform workflows (init, plan, apply) 
    from within the Platform Engine.
    """
    infra_dir = os.path.abspath("infra")
    
    # 1. Map the command
    if action == "init":
        command = ["terraform", "init"]
    elif action == "plan":
        command = ["terraform", "plan"]
    elif action == "apply":
        # -auto-approve is critical for platform automation
        command = ["terraform", "apply", "-auto-approve"]
    else:
        print(f"Unknown action: {action}")
        return

    print(f"--- Running Terraform {action.upper()} ---")
    
    # 2. Execute and stream the output (SRE Observability)
    try:
        process = subprocess.Popen(
            command,
            cwd=infra_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        for line in process.stdout:
            print(line, end="")

        process.wait()
        
        if process.returncode == 0:
            print(f"--- {action.upper()} COMPLETED SUCCESSFULLY ---")
        else:
            print(f"--- {action.upper()} FAILED with exit code {process.returncode} ---")
            
    except Exception as e:
        print(f"Error executing Terraform: {e}")

if __name__ == "__main__":
    # Standard Platform Workflow: APPLY
    # This officially provisions the infrastructure in AWS
    run_terraform_action("apply")