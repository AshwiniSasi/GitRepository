from git import Repo

# Define the local repository directory

REPO_DIR = "/home/user/automation"  # Replace with your local repo path

COMMIT_MESSAGE = "first commit"

TOKEN = "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"  # Replace with your GitHub personal access token

USERNAME = "AshwiniSasi"  # Replace with your GitHub username

REPO_NAME = "GitRepository.git"  # Replace with your repository name
BRANCH_NAME = "master"


# Construct the remote URL with the token

REMOTE_URL = f"https://{USERNAME}:{TOKEN}@github.com/{USERNAME}/{REPO_NAME}"

print(REMOTE_URL)

# Open the existing repository

repo = Repo.init(REPO_DIR)



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
            #origin.push('--set-upstream', origin.name, repo.active_branch.name)
            result = origin.push(refspec=f"{repo.active_branch.name}:refs/heads/{repo.active_branch.name}", set_upstream=True, force=True)
            for push_info in push_info_list:

                print(f"Push update: {push_info.summary}")

                if push_info.flags & push_info.ERROR:

                    print(f"Error occurred during push: {push_info.summary}")

                elif push_info.flags & push_info.REJECTED:

                     print(f"Push rejected: {push_info.summary}")

                elif push_info.flags & push_info.UP_TO_DATE:

                    print("Branch is already up-to-date.")
 
                else:
                    print(f"Push successful: {push_info.summary}")
                    print(result)
                    print("Changes pushed to the remote repository.")
        except Exception as e:

            print(f"An error occurred while pushing the changes: {e}")

    

    except Exception as e:

        print(f"An error occurred while committing the changes: {e}")
