import click
import sys
from app.engine import generate_terraform_file
from app.deployer import run_terraform_action
from app.monitor import check_platform_health

@click.group()
def cli():
    """
    Sentinel Platform CLI: The Self-Service Internal Developer Platform.
    """
    pass

@cli.command()
@click.option('--name', prompt='Project Name', help='The name of the project')
@click.option('--owner', prompt='Owner Name', help='The developer requesting the infra')
def provision(name, owner):
    """
    Standard Operating Procedure: Provisions a compliant environment.
    """
    click.secho(f"\nReceived Platform Request for: {name}", fg='green', bold=True)
    
    # Step 1: Engine (Templating)
    click.secho("\n--- [Step 1] Generating Infrastructure Blueprint ---", fg='blue')
    try:
        generate_terraform_file(name, owner)
    except Exception as e:
        click.secho(f"Error generating blueprint: {e}", fg='red')
        sys.exit(1)
    
    # Step 2: Deployer (Init & Plan)
    click.secho("\n--- [Step 2] Initializing Platform Engine ---", fg='blue')
    run_terraform_action("init")
    
    click.secho("\n--- [Step 3] Validating Configuration (Plan) ---", fg='blue')
    run_terraform_action("plan")
    
    # Step 3: Human-in-the-Loop Confirmation
    if click.confirm('\nDo you want to apply this configuration to AWS Production?', default=True):
        click.secho("\n--- [Step 4] Provisioning Resources (Apply) ---", fg='blue')
        run_terraform_action("apply")
        
        # Step 4: Monitor (SRE Check)
        click.secho("\n--- [Step 5] Verifying Service Level Objectives (SLOs) ---", fg='blue')
        success = check_platform_health(name)
        
        if success:
            click.secho(f"\nSUCCESS: Project '{name}' is live and healthy.", fg='green', bold=True)
        else:
            click.secho(f"\nFAILURE: Project '{name}' failed health checks.", fg='red', bold=True)
    else:
        click.secho("\nOperation cancelled by user.", fg='yellow')

if __name__ == "__main__":
    cli()