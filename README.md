# dsa5106-convnext-extension

## Local Setup
### Environment and extension
In your VSCode, if you're developing locally,
1. Install `ruff` extension, this helps linting your Python code.
2. Install `uv` (can use brew or any other method you prefer), we'll use this to manage our environments instead of pip (both in VSCode and in Kaggle Notebook).
3. Some basic libraries and dependencies have been added to `pyproject.toml` and locked under `uv.lock`. You can start a new virtual environment by typing `uv venv` in the project root and then activate that virtual environment (typically by doing `source ~/<your_path_to_this_folder>/.venv/bin/activate`). Tips: to automatically select the venv everytime you open this project, open the command palate (Cmd + Shift + p) > Python: Select Interpreter > Enter interpreter path... > put `.venv/bin/activate` as the path > Enter. Open a new terminal window in VSCode, then you should be in your venv already (one easy way to verify is to run `which python3`, it should point to the python3 version in your venv path).
4. Start syncing the dependencies by using `uv sync`.
5. If you want to add new libraries, you can do so by adding `uv add <package>`. This will automatically update the lockfile (`uv.lock` and `pyproject.toml`). If you're updating the `pyproject.toml` in your pull requests, add somebody else as the reviewer of the pull request and inform people to update their environment accordingly. This is to prevent environment conflicts. 

### Further things on Linting
1. Create a `.vscode` folder in the project root. 
2. Create a file `settings.json`. Add this to the file:
```json
{
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.codeActionsOnSave": {
        "source.fixAll": "explicit",
        "source.organizeImports": "explicit"
        }
    },
    "ruff.configuration": "pyproject.toml"
}
```

## Git workflow
1. Create a new branch, based off the main branch.
2. Add, commit, and push your changes to that branch.
3. Create a pull request.
4. If you're updating the `pyproject.toml`/any other shared files in your pull requests, add somebody else as the reviewer of the pull request. Else, just merge the commit to the main branch directly by yourself. 

Idea: At the initial stages, we can just push our individual file into `tmp_notebook` folder. Then the consolidation team will help to refactor the notebooks into ready-to-use Python scripts. 
Note: always remember to keep your branch and main branch up-to-date by using git pull!

## Using this repository in Kaggle/Colab notebook
1. uv setup
```python
# 1. Install uv (it's a standalone binary, very fast)
!curl -LsSf https://astral.sh/uv/install.sh | sh
import os
os.environ["PATH"] += ":" + os.path.expanduser("~/.cargo/bin")

# 2. Clone your project
!git clone git@github.com:angeladianas/dsa5106-convnext-extension.git
%cd dsa5106-convnext-extension

# 3. Sync the environment using uv
!uv pip sync uv.lock --system

# 3. or can use
!uv pip install -r pyproject.toml --system
```

2. If you want to install new libraries

```python
# 1. Install the new library and update the lockfile
!uv add <package> --raw-sources

# 2. Verify the lockfile was updated
# NOTE: this does not mean you have updated your lockfile in git. You still need to push your changes as per the git workflow.
!ls -l uv.lock
```
