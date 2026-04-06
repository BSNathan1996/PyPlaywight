
# PyPlaywright

A Python testing project using Pytest and Playwright for automated browser testing.

## Overview

This project runs automated tests on pushes and pull requests to `main` and `master` branches using GitHub Actions.

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

## CI/CD

Tests run automatically on:
- Push to `main` or `master`
- Pull requests to `main` or `master`

**Timeout:** 60 minutes per run

**Test reports** are uploaded as artifacts and retained for 30 days.
