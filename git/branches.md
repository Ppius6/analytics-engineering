# Creating a feature branch, working on it, and merging into main

## 1. Create and switch to a new branch

```bash
git checkout -b feature-branch-name
```

Or with newer Git syntax:

```bash
git switch -c feature-branch-name
```

## 2. Make changes and commit

After making your changes:

```bash
# Stage all changes
git add .

# Commit with a descriptive message
git commit -m "Add feature description"
```

## 3. Push branch to GitHub

First time pushing the branch:

```bash
git push -u origin feature-branch-name
```

For subsequent pushes:

```bash
git push
```

## 4. Merge with main

### Option A: GitHub Pull Request (Recommended)

1. Go to your GitHub repository
2. Click "New Pull Request"
3. Select your branch to merge into main
4. Create and merge the PR

### Option B: Local merge

```bash
# Switch to main
git checkout main

# Pull latest changes
git pull origin main

# Merge your feature branch
git merge feature-branch-name

# Push updated main
git push origin main
```

## 5. Clean up (Optional)

Delete local branch:

```bash
git branch -d feature-branch-name
```

Delete remote branch:

```bash
git push origin --delete feature-branch-name
```

## Tips

- Use descriptive branch names: `feature/user-login`, `fix/header-bug`
- Always pull latest main before creating a new branch
- Write clear commit messages
- Deleting branches after merge is optional but keeps the repo clean
