import unittest
from unittest.mock import patch, mock_open
from app.engine import generate_terraform_file

class TestPlatformEngine(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    @patch("app.engine.Environment") # Mock Jinja2 so we don't need real templates
    def test_terraform_generation(self, mock_env, mock_file):
        """
        Unit Test: Verifies that the Platform Engine attempts to write 
        a Terraform file with the correct parameters.
        """
        # Setup the mock template
        mock_template = mock_env.return_value.get_template.return_value
        mock_template.render.return_value = 'resource "aws_vpc" "test" {}'

        # Execute the function
        generate_terraform_file("Test-Project", "Test-Owner")

        # Assertions (The Test)
        # 1. Did it try to open 'infra/main.tf' for writing?
        mock_file.assert_called_with("infra/main.tf", "w")
        
        # 2. Did it try to load the correct template?
        mock_env.return_value.get_template.assert_called_with('vpc_template.tf.j2')
        
        # 3. Did it render with the correct context data?
        # We check the arguments passed to render()
        call_args = mock_template.render.call_args[0][0]
        self.assertEqual(call_args['project_name'], "Test-Project")
        self.assertEqual(call_args['developer_name'], "Test-Owner")

if __name__ == "__main__":
    unittest.main()