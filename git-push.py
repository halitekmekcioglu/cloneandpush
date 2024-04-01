import subprocess
import os

def git_push(folder_path, commit_message, remote_name="origin", remote_url=None, user_name=None, user_email=None):
    # Change to the directory
    os.chdir(folder_path)

    # Set the user name and email if provided
    if user_name and user_email:
        subprocess.check_call(["git", "config", "user.name", user_name])
        subprocess.check_call(["git", "config", "user.email", user_email])

    # Run the git commands
    try:
        if remote_url:
            try:
                subprocess.check_call(["git", "remote", "add", remote_name, remote_url])
            except subprocess.CalledProcessError:
                subprocess.check_call(["git", "remote", "set-url", remote_name, remote_url])
        subprocess.check_call(["git", "add", "--all"])
        subprocess.check_call(["git", "commit", "-m", commit_message])
        subprocess.check_call(["git", "push", remote_name])
        print("Pushed to remote repository successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to push to remote repository. Error: ", e)

# Usage
folder_path = "C:\\Users\\xxx\\OneDrive\\Masaüstü\\folder"
commit_message = input("Enter commit message: ")
remote_url = "https://github.com/xxx/Projects"  # Replace with your GitHub repo URL
user_name = "your user name"  # Replace with your name
user_email = "yourmail "  # Replace with your email
git_push(folder_path, commit_message, remote_url=remote_url, user_name=user_name, user_email=user_email)