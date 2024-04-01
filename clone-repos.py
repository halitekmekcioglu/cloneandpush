import subprocess

# Destination folder where the repository will be cloned
destination_folder = r"C:\Users\xxx\OneDrive\Masaüstü\folder"

# Git clone command with repository URL
repository_url = "https://github.com/xxxx/Projects.git"
clone_command = ["git", "clone", repository_url, destination_folder]

try:
    # Execute the clone command using subprocess
    subprocess.run(clone_command, check=True)
    print("Repository cloned successfully!")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
    # Handle authentication failure or other errors here
