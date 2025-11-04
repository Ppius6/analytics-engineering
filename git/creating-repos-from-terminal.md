# Creating a GitHub repository from the terminal

## Prerequisites

- GitHub CLI installed (`gh`)
- Authenticated with GitHub (`gh auth login`)

## Method 1: Using GitHub CLI (Recommended)

### Start with existing project

```bash
# Navigate to your project directory
cd your-project-folder

# Initialize git if not already done
git init

# Add and commit your files
git add .
git commit -m "Initial commit"

# Create GitHub repo and push
gh repo create your-repo-name --public --push
```

### Start from scratch

```bash
# Create and navigate to new directory
mkdir your-project-name
cd your-project-name

# Initialize git
git init

# Create a README file
echo "# Your Project Name" > README.md

# Add and commit
git add .
git commit -m "Initial commit"

# Create GitHub repo and push the changes
# Public
gh repo create analytics-engineering --public --source=. --remote=origin --push
# Private
gh repo create analytics-engineering --private --source=. --remote=origin --push
```

## Method 2: Manual approach

### 1. Create repository on GitHub

- Go to github.com
- Click "New repository"
- Fill in repository name and settings
- Click "Create repository"

### 2. Connect local project

```bash
# Navigate to your project
cd your-project-folder

# Initialize git (if not done)
git init

# Add remote origin
git remote add origin https://github.com/username/repo-name.git

# Add and commit files
git add .
git commit -m "Initial commit"

# Push to GitHub
git branch -M main
git push -u origin main
```

## GitHub CLI Options

Common flags for `gh repo create`:

- `--public` - Make repository public
- `--private` - Make repository private
- `--push` - Push local commits to new repository
- `--clone` - Clone the repository locally
- `--description "text"` - Add repository description

## Installing GitHub CLI

### macOS

```bash
brew install gh
```

### Ubuntu/Debian

```bash
sudo apt install gh
```

### Windows

Download from: <https://cli.github.com/>

## Authentication

```bash
gh auth login
```

Follow the prompts to authenticate with your GitHub account.
