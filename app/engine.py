import os
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv

load_dotenv()

def generate_terraform_file(project_name, developer_name, cidr="10.0.0.0/16"):
    """
    Acts as the 'Platform Engine' by generating a custom 
    Terraform file from a standard template.
    """
    # 1. Setup the template environment
    file_loader = FileSystemLoader('app/templates')
    env = Environment(loader=file_loader)
    
    # 2. Load the Gold Standard VPC template
    template = env.get_template('vpc_template.tf.j2')
    
    # 3. Define the data (The 'Product' configuration)
    context = {
        "region": os.getenv("AWS_REGION", "eu-west-1"),
        "project_name": project_name,
        "developer_name": developer_name,
        "cidr": cidr
    }
    
    # 4. Render the template into a real .tf file
    output = template.render(context)
    
    # 5. Save the file to the infrastructure folder
    with open("infra/main.tf", "w") as f:
        f.write(output)
    
    print(f"Success: Infrastructure blueprint created for project '{project_name}'.")

if __name__ == "__main__":
    # Test run: simulate a developer named Love requesting a project
    generate_terraform_file(
        project_name="Lagos-Hub", 
        developer_name="Love-Arinze"
    )