import os
import re
import sys
import argparse

def update_version(environment, module_name, new_version):
    # Determine the file path
    file_path = f"environments/{environment}/main.tf"
    if not os.path.exists(file_path):
        print(f"Error: Could not find configuration for environment '{environment}' at {file_path}")
        sys.exit(1)

    with open(file_path, 'r') as f:
        content = f.read()

    # Regex to match the source line and capture the ref value for the specific module
    # Example snippet: source = "git::https://github.com/org/repo.git//modules/example?ref=v1.0.0"
    pattern = rf'(source\s*=\s*"[^"]*?//modules/{re.escape(module_name)}\?ref=)([^"]+)(")'
    
    if not re.search(pattern, content):
        print(f"Error: Could not find a valid source reference for module '{module_name}' in {file_path}")
        sys.exit(1)

    new_content = re.sub(pattern, rf'\g<1>{new_version}\g<3>', content)

    if new_content == content:
        print(f"Module '{module_name}' in '{environment}' is already at version '{new_version}'. No changes made.")
        sys.exit(0)

    with open(file_path, 'w') as f:
        f.write(new_content)

    print(f"Successfully updated '{module_name}' in '{environment}' to version '{new_version}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update Terraform module version.")
    parser.add_argument("--env", required=True, help="Target environment (e.g., dev, staging, prod)")
    parser.add_argument("--module", required=True, help="Name of the module to update")
    parser.add_argument("--version", required=True, help="New version tag (e.g., v1.2.3)")

    args = parser.parse_args()
    update_version(args.env, args.module, args.version)
