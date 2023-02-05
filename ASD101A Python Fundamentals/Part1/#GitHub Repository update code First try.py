#GitHub Repository update code First try/Version 1

from git import Repo

# specify the local file folder and the GitHub repository URL
local_folder = '/path/to/local/folder'
git_repo = 'https://github.com/username/repository.git'

# initialize git repository in the local folder
repo = Repo(local_folder)

# add all modified and deleted files in the local folder to the git repository
repo.git.add(u=True)

# create a new commit with a message
repo.index.commit("Sync files")

# add the remote GitHub repository as the origin
origin = repo.create_remote('origin', git_repo)

# push the local repository to the remote GitHub repository
origin.push()

