# E-soko
# E-Sokoo Project README

## Overview

This README provides detailed steps for completing tasks related to cloning, forking, managing branches, handling conflicts, enabling GitHub Pages, and exploring open-source contributions using the E-Sokoo project.

## Prerequisites

- A GitHub account
- Git installed on your local machine
- A code editor (e.g., Visual Studio Code, Sublime Text)
- Ubuntu operating system

## Task 1: Cloning and Forking

### Cloning a Repository

1. **Choose a public GitHub repository:**
   - I chose the E-Sokoo project.

2. **Clone the repository to your local machine:**
   ```bash
   git clone https://github.com/original-repository/e-sokoo.git
   ```

3. **Explore the repository:**
   - Navigate the file structure, examine the files, and review the commit history using Git commands like `git log` and `git status`.

### Forking a Repository

1. **Fork the repository:**
   - On the GitHub page of the E-Sokoo project, click the "Fork" button to create a copy of the repository under your GitHub account.

2. **Clone the forked repository to your local machine:**
   ```bash
   git clone https://github.com/your-username/e-sokoo.git
   ```

## Task 2: Managing Branches

### Creating and Switching Branches

1. **Create a new branch:**
   ```bash
   cd e-sokoo
   git checkout -b feature-update
   ```

2. **Switch to the newly created branch:**
   - This is already done by the `git checkout -b` command.

### Making Changes and Committing

1. **Make changes to a file or add a new file:**
   - Edit an existing file or create a new file, for example, `new-feature.txt`.

2. **Commit the changes:**
   ```bash
   git add new-feature.txt
   git commit -m "Added new feature"
   ```

### Merging Changes

1. **Switch back to the main branch:**
   ```bash
   git checkout main
   ```

2. **Merge the changes from the `feature-update` branch:**
   ```bash
   git merge feature-update
   ```

## Task 3: Handling Conflicts

### Creating Conflicts

1. **In your forked repository, make changes to the same file modified in Task 4:**
   - Modify a file in the `main` branch and commit the changes.

2. **Commit the changes:**
   ```bash
   git add conflicting-file.txt
   git commit -m "Made conflicting changes"
   ```

### Resolving Conflicts

1. **Create a new branch to resolve the conflict:**
   ```bash
   git checkout -b resolve-conflict
   ```

2. **Resolve the conflict manually in the file:**
   - Open the conflicting file, edit the conflicting sections, and save the file.

3. **Commit the changes and merge the branch back into `main`:**
   ```bash
   git add conflicting-file.txt
   git commit -m "Resolved conflict"
   git checkout main
   git merge resolve-conflict
   ```

## Task 4: GitHub Pages

### Enabling GitHub Pages

1. **Create a simple HTML file:**
   - Create an `index.html` file in the repository root.
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>E-Sokoo</title>
   </head>
   <body>
       <h1>Welcome to E-Sokoo</h1>
       <p>This is a sample GitHub Page for the E-Sokoo project.</p>
   </body>
   </html>
   ```

2. **Enable GitHub Pages:**
   - Go to the repository settings on GitHub.
   - Scroll down to the "GitHub Pages" section.
   - Set the source to the `main` branch and save.

### Accessing the Published Page

1. **Visit the GitHub Pages URL:**
   - The URL is typically `https://your-username.github.io/e-sokoo/`
   - Verify that the `index.html` file is accessible online.

## Task 5: Open Source Exploration

### Exploring Open Source Projects

1. **Search for an open-source project on GitHub:**
   - Find a project related to your interests by using GitHub's search and filtering options.
   - I used 'web development' project by kit

2. **Explore the project's documentation, issues, and contribution guidelines:**
   - Read the `README.md`, `CONTRIBUTING.md`, and browse the issues tab.

### Opening an Issue

1. **Open a new issue in the chosen open-source project:**
   - Go to the "Issues" tab of the repository.
   - Click "New issue" and fill out the template with your suggestion, bug report, or question.
   - Submit the issue.

## Submission

- Push all changes to your forked repository:
  ```bash
  git push origin main
  ```

- Share the link to your forked repository: https://neemamwende.github.io/E-sokoo/

This assignment provided hands-on experience with Git, GitHub, and open-source practices, covering various aspects essential for software development and collaboration.
