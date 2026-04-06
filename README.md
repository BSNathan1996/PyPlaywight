
# PyPlaywright

A Python testing project using Pytest and Playwright for automated browser testing.
Base URL = "https://www.qaplayground.com/practice"

## Overview

This project runs automated tests on pushes and pull requests to `main` branche using GitHub Actions.

## Setup

### Requirements
- Python 3.12
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the repository
2. Install dependencies:
    ```bash
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    python -m playwright install
    ```

## Testing

Run tests locally:
```bash
python -m pytest
```

Run tests locally in headed mode:
```bash
python -m pytest --headed
```
Run tests locally for a specified marker:
```bash
python -m pytest -m <markerName>
```

## CI/CD

Tests run automatically on `main`:

Walkthrough for using Version Control
- Create a branch of your own
```bash
git branch <BranchName>
```
- Switch to your branch
```bash
git checkout <BranchName>
```
- Move all the codes to Staging phase
```bash
git add .
```
- Commit all the staged code with a message[Required]
```bash
git commit -m "Commit message"
```
- Push Code[First time]
```bash
git push -u origin <branch-name>: 
```

**Timeout:** 60 minutes per run

**Test reports** are uploaded as artifacts and retained for 30 days.