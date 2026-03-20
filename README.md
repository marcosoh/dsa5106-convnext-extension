# DSA5106 Modernising ConvNets: Reproducing & Extending the ConvNeXt Architecture

This repository contains the official implementation and research findings for our project in DSA5106: Deep Learning. Our work focuses on the ConvNeXt architecture—a pure convolutional network designed to compete with hierarchical Vision Transformers (ViTs) by adopting modern training techniques and architectural design choices.

## Project Overview
The core objective of this research is to evaluate the scalability and generalizability of the ConvNeXt design philosophy. We move beyond the original paper's ImageNet-1K focus to test these modernised CNN principles in data-constrained (low-regime) settings.

**Our project is structured into four key pillars:**
- Reproduction: Re-implementing the ConvNeXt-Tiny pipeline on the CIFAR-100 dataset to verify core performance claims.
- Extension 1 (Augmentation Ablation): Quantifying the marginal contributions of geometric versus mixture-based data augmentation strategies.
- Extension 2 (Architectural Verification): Independently verifying micro-design ablations (e.g., LayerNorm vs. BatchNorm, GELU vs. ReLU) at a smaller scale.
- Extension 3 (Cross-Domain Transfer): Evaluating the architecture's efficacy in medical imaging by fine-tuning on the HAM10000 skin lesion dataset.

**Key Findings**
- Performance: Our ConvNeXt-Tiny reproduction achieved a Top-1 Accuracy of 90.47% on the HAM10000 dataset, significantly outperforming ResNet-50 and Swin-Transformer baselines.
- Robustness: Despite the class imbalance inherent in medical imaging, the model maintained a high Macro F1-score of 0.835, indicating strong performance across both majority and minority classes.
- Design Generalization: Our architectural ablations confirm that design choices like the inverted bottleneck and LayerNorm provide tangible benefits even when transitioned from high-resolution natural images to specialized low-resolution benchmarks.

**Contributors**
Ashley Lim Zhi Yan, Chen Yao Quan, Diana, Marco, Poh Yu Jie, Tan Yi Kai, Zhang Jia Wen

**Repository Structure**
```
DSA5106-CONVNEXT-EXTENSION
├── logs/                          # Training and experiment logs
├── notebook/                      # Research and experiment notebooks
│   ├── extension-1a-convnext-baseline.ipynb
│   ├── extension-1b-geometric-augmentation.ipynb
│   ├── extension-1c-mixture-augmentation.ipynb
│   ├── extension-1d-full-recipe.ipynb
│   ├── extension-2a-batchnorm.ipynb
│   ├── extension-2b-relu.ipynb
│   ├── extension-2c-1x1conv.ipynb
│   ├── extension-3a-confusion-matrix.ipynb
│   ├── extension-3a-convnext-tiny.ipynb
│   ├── extension-3b-resnet50.ipynb
│   ├── extension-3bcd-confusion-matrix.ipynb
│   ├── extension-3c-swintiny-default.ipynb
│   └── extension-3d-swintiny-optimised.ipynb
├── results/                       # Output artifacts
│   ├── images/                    # Generated plots and figures
│   ├── __init__.py
│   └── results_from_logs.ipynb    # Parsed logs
├── tmp_notebook/                  # Temporary or scratchpad notebooks
├── utils/                         # Utility scripts and helper functions
│   ├── __init__.py
│   └── logs_parser.py
├── .gitignore                     # Git ignore file
├── LICENSE                        # Project license
├── README.md                      # Project documentation
├── __init__.py
├── pyproject.toml                 # Project metadata and dependencies
└── uv.lock                        # UV package manager lockfile
```

## Development Guide
Setup guidelines to ensure that we have the same environment and code linting.

### 1. Local Setup
---
#### a. Environment and extension
In your VSCode, if you're developing locally,
1. Install `ruff` extension, this helps linting your Python code.
2. Install `uv` (can use brew or any other method you prefer), we'll use this to manage our environments instead of pip (both in VSCode and in Kaggle Notebook).
3. Some basic libraries and dependencies have been added to `pyproject.toml` and locked under `uv.lock`. You can start a new virtual environment by typing `uv venv` in the project root and then activate that virtual environment (typically by doing `source ~/<your_path_to_this_folder>/.venv/bin/activate`). Tips: to automatically select the venv everytime you open this project, open the command palate (Cmd + Shift + p) > Python: Select Interpreter > Enter interpreter path... > put `.venv/bin/activate` as the path > Enter. Open a new terminal window in VSCode, then you should be in your venv already (one easy way to verify is to run `which python3`, it should point to the python3 version in your venv path).
4. Start syncing the dependencies by using `uv sync`.
5. If you want to add new libraries, you can do so by adding `uv add <package>`. This will automatically update the lockfile (`uv.lock` and `pyproject.toml`). If you're updating the `pyproject.toml` in your pull requests, add somebody else as the reviewer of the pull request and inform people to update their environment accordingly. This is to prevent environment conflicts. 
6. Run this at project root so that you can import `utils/` from other folders in this repository: `uv pip install -e .`.

#### b. Further things on Linting
This is more important for those doing the results consolidation and anyone creating the templates for others to use. This is to ensure that we all have a similar code style.
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

### 2. Git workflow
---
1. Create a new branch, based off the main branch.
2. Add, commit, and push your changes to that branch.
3. Create a pull request.
4. If you're updating the `pyproject.toml`/any other shared files in your pull requests, add somebody else as the reviewer of the pull request. Else, just merge the commit to the main branch directly by yourself. 

Idea: At the initial stages, we can just push our individual file into `tmp_notebook` folder. Then the consolidation team will help to refactor the notebooks into ready-to-use Python scripts. 
Note: always remember to keep your branch and main branch up-to-date by using git pull!
For branching strategies, up to your preference. You can always create a new branch based off main for every changes you created. Or you can create a long-lived branch. 

```bash
# 1. Go to the main branch
git checkout main

# 2. Pull changes from main
git pull origin main

# 3. Create and checkout to a new branch (replace your_branch_name with your desired branch name)
git checkout -b your_branch_name

# 4. Add changes
git add xyz.py

# 5. Commit changes, add your commit message
git commit -m "feat: your commit message"

# 6. Push the changes
git push origin your_branch_name

# 7. Go to Github and create your pull request
```

### 3. Using this repository in Kaggle notebook
---
1. Link your Kaggle notebook with your Github account (Notebook > File > Link to Github). You also need to create a PAT (Personal Access Token) in Github so that you do not need to repeatedly enter your credentials when connecting to Github from Kaggle. Steps:
- Go to your Github Settings > Developer Settings > Tokens (Classic) > Generate new token (Fine grained, repo-scope) > Set everything up (Permissions needed: Contents (Read only)). 
- Do not push your changes from Kaggle notebook, so to avoid this mistake, we set the Permissions to just read only. 
- Copy and save the token.
- Go to your Kaggle notebook again > Add-ons > Secrets > Add a secret named `GH_TOKEN` and add your github token.
2. Turn on your internet access in the notebook (Settings > Turn on internet).
3. Setup
```python
from kaggle_secrets import UserSecretsClient
import os

# 1. Get the token safely
user_secrets = UserSecretsClient()
token = user_secrets.get_secret("GH_TOKEN")
repo_name = "dsa5106-convnext-extension"

# 2. Construct the URL with the token
repo_url = f"https://angeladianas:{token}@github.com/angeladianas/{repo_name}.git"

# 3. Clone without being asked for a username
if not os.path.exists(repo_name):
    print("Cloning private repository...")
    !git clone {repo_url}
else:
    print("Repo already exists. Pulling latest...")
    %cd {repo_name}
    !git pull {repo_url} origin main

%cd {repo_name}

!uv pip install -r pyproject.toml --system
```

2. If you want to install new libraries, you can use uv add. Then let Diana knows on what new libraries you need and she'll add it to the `pyproject.toml` and `uv.lock`.

```python
# 1. Install the new library and update the lockfile
!uv add <package>

# 2. Verify the lockfile was updated
# NOTE: this does not mean you have updated your lockfile in git. You still need to push your changes as per the git workflow.
!ls -l uv.lock
```

## Disclaimer
---
AI is used in generating docstring, enhancing the sentences, and other formatting. 