from git import Repo

import os



# Define the local repository directory and the commit message

REPO_DIR = "/path/to/your/local/repo"  # Replace with the path to your local repo

COMMIT_MESSAGE = "Your commit message here"

REMOTE_URL = "https://github.com/your-username/your-repo.git"  # Replace with your remote repository URL



# Open the existing repository

repo = Repo(REPO_DIR)



# Check if the repository is valid

if repo.bare:

    print(f"Repository {REPO_DIR} is not valid.")

else:

    try:

        # Ensure a remote named 'origin' exists, and set its URL

        if 'origin' not in [remote.name for remote in repo.remotes]:

            repo.create_remote('origin', REMOTE_URL)

        else:

            repo.remotes.origin.set_url(REMOTE_URL)



        # Stage the changes (equivalent to `git add .`)

        repo.git.add(A=True)  # 'A=True' stages all changes



        # Commit the changes

        commit = repo.index.commit(COMMIT_MESSAGE)

        print(f"Committed changes with commit ID: {commit.hexsha}")



        # Push changes to the remote repository

        try:

            origin = repo.remote(name='origin')

            origin.push()

            print("Changes pushed to the remote repository.")

        except Exception as e:

            print(f"An error occurred while pushing the changes: {e}")

    

    except Exception as e:

        print(f"An error occurred while committing the changes: {e}")
