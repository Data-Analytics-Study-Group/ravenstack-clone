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
`git checkout -b prefix/purpose-description`
Example:
`git checkout -b data/data-cleaning`

Please see 'Branch Naming Convention' below for more information.

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


## Branch Naming Convention

| Prefix | Purpose |
|--------|---------|
| `data/` | Data cleaning or pipeline changes |
| `explore/` | EDA or one-off investigations |
| `pipeline/` | ETL/ELT workflows and orchestration (Airflow, dbt, etc.) |
| `fix/` | Fixing a bug in code, a broken pipeline, or bad logic |
| `docs/` | READMEs, data dictionaries, methodology writeups |
| `eval/` | Model evaluation, metrics, and validation work |
| `viz/` | Dashboards, charts, and reporting visuals |

### Rules for the Description
- **2–5 words max** — keep it concise
- **Use imperative form** — `normalize-sales-schema` not `normalized-sales-schema`
- **Use lowercase with hyphens (kebab-case)** — `fix-null-join-logic` not `Fix_Null_Join_Logic`
- **Be precise** — anyone reading the branch name should know what it adds to the project
- **Avoid vague names** — `fix/updates` or `data/changes` tells nobody anything

### Examples

| ✅ Good | ❌ Bad |
|--------|--------|
| `data/normalize-sales-schema` | `data/changes` |
| `explore/customer-churn-patterns` | `explore/analysis` |
| `pipeline/daily-revenue-aggregation` | `pipeline/new-pipeline` |
| `fix/null-handling-join-step` | `fix/bug` |
| `viz/executive-kpi-dashboard` | `viz/dashboard2` |


## Git Workflow
### Rule: Always commit on your feature branch, never directly on main.  

For a detailed guide on working with branches and Pull Requests, see the [Version Control Guide](version-control.md).

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
4. Select the appropriate milestone
4. Provide a clear description, including:
   - What the issue is
   - Why it matters
   - Steps to reproduce (if applicable)

---

### Linking Issues to Work

When working on an issue:

- Create a feature branch for the task.
- Open a Pull Request (PR) when the work is ready.
- Reference the issue number in the PR description when applicable.
- When the PR is merged into main, GitHub automatically closes all three issues in the example below.Git scans the PR description and automatically closes the issue when it detects these keywords:

Example:

```text
#To link to and close an issue:
Closes #12
Resolves #11
Fixes #15

#To link to an issue but not close it:
#8
Related to #5
```

### Notes

This project is currently under active development, so guidelines may evolve over time.
