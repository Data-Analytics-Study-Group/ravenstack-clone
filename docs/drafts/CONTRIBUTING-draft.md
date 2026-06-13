# Contributing Guidelines

Thank you for considering contributing to this project.

This document outlines the basic workflow and standards for contributing to the repository.

---

## Getting Started

1. Clone the repository:
```bash
git clone <https://github.com/Data-Analytics-Study-Group/ravenstack-pl.git>
cd <ravenstack-pl>
```

2. Create a new branch for your work:
`git checkout -b your-name/feature-description`

3. Install dependencies (if applicable):
`pip install -r requirements.txt`

4. Set up environment variables:
- Copy `.env.example` to `.env`
- Add required values (e.g. `DATABASE_URL` for Neon)


## Security Guidelines

- Never commit secrets or API keys
- Use .env for sensitive information
- Do not expose credentials in notebooks or logs


## Coding Standards

### Code Style

- Write clear, readable code.
- Follow consistent naming conventions.
- Use lowercase letters and underscores (snake_case) for variables and functions.
- Use meaningful variable and function names.

### Project Structure

- Place raw data in data/raw/
- Place intermediate data in data/interim/
- Place processed data in data/processed/
- Keep notebooks in notebooks/
- Keep reusable code in src/

## Security Guidelines

- Never commit secrets or API keys
- Use .env for sensitive information
- Do not expose credentials in notebooks or logs


## File and Folder Naming Conventions  

To maintain consistency across the project, follow these naming guidelines:

### Folders

- Use lowercase letters and underscores (snake_case).
- Avoid spaces and special characters.

Examples:  
- data_quality
- feature_engineering
- model_evaluation


### Python Files

- Use lowercase letters and underscores (snake_case).
- File names should describe their purpose.

Examples:
- data_cleaning.py
- feature_engineering.py
- train_model.py


### Notebooks 

- Use descriptive names.
- Use lowercase letters and underscores (snake_case).
- Prefer a numeric prefix to indicate workflow order.

Examples:

- 01_data_exploration.ipynb
- 02_data_cleaning.ipynb
- 03_model_training.ipynb

### Data Files

- Use lowercase letters and underscores.
- Include dates where appropriate using the format YYYY_MM_DD.

Examples:

- customer_data.csv
- usage_data_2026_06_12.csv


### Documentation Files

- Use lowercase letters and hyphens (kebab-case).

Examples:

- data-quality-report.md
- smart-framework.pdf


## Branch Names
- Use lowercase letters and hyphens (kebab-case).

Examples:

- your-name/feature-description
- feature/usage-cleaning
- bugfix/missing-user-ids


## Git Workflow

1. Make changes in a feature branch
2. Commit changes with clear messages
3. Push your branch to GitHub
4. Open a Pull Request (PR)
5. Request review before merging


## Pull Requests

- Keep PRs small and focused
- Describe what changes were made and why
- Link related issues when applicable


## Issues

- Use GitHub Issues to report bugs or request features
- Provide clear descriptions and context when opening an issue


## Working with Issues

GitHub Issues are used to track all tasks, bugs, features, and discussions in this project.

### Before You Start Work

1. Check the **Issues** tab in the repository
2. Look for an issue you want to work on
3. Make sure it is not already assigned to someone else
4. If appropriate, assign yourself to the issue

---

### Creating a New Issue

If you identify a bug, improvement, or task that is not listed:

1. Go to the **Issues** tab
2. Click **New Issue**
3. Select the appropriate label (e.g. `bug`, `feature`, `discussion`)
4. Provide a clear description, including:
   - What the issue is
   - Why it matters
   - Steps to reproduce (if applicable)

---

### Linking Issues to Work

When starting work on an issue:

- Create a new branch for the task
- Reference the issue number in your branch or commit messages

Example:

```bash id="r7qz1m"
git checkout -b feature/usage-cleaning-#12
```

### Notes

This project is currently under active development, so guidelines may evolve over time.