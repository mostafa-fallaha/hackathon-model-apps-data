import subprocess
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Run DVC and Git commands.")
parser.add_argument("commit_message", type=str, help="Commit message for Git")
args = parser.parse_args()

# Define variables
data_file = "data/googleplaystore_model_cleaned.csv"
dvc_file = "data/googleplaystore_model_cleaned.csv.dvc"
gitignore_file = "data/.gitignore"
# script_file = "version_data_apps.py"
commit_message = args.commit_message

# Run DVC and Git commands
subprocess.run(["dvc", "add", data_file], check=True)
subprocess.run(["git", "add", dvc_file, gitignore_file, 'run_versioning_model_data.ps1', '.dvc/config',
                'version_model_data.py', 'README.md', 'clean_for_model.ipynb', '.gitignore'], check=True)
subprocess.run(["git", "commit", "-m", commit_message], check=True)
subprocess.run(["dvc", "push"], check=True)
subprocess.run(["git", "push"], check=True)
