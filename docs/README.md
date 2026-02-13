# Full-Stack Web Application

This repository contains a full-stack web application built with Node.js,
Express, and SQLite. It includes scripts and documentation for setting up,
configuring, and deploying the application on an AWS EC2 instance.

- [Development Guide](dev-node/README.md)
- [Deployment Guide (Docker)](deploy-docker/README.md)
- [Deployment Guide (Manual)](deploy-node/README.md)

## Technology Stack

- Backend technology stack
    - Backend Runtime: [Python](https://www.python.org/) 3.x
    - Backend Framework: [Django](https://www.djangoproject.com/)
    - Database: [SQLite](https://www.sqlite.org/index.html) for lightweight data storage
- Frontend technology stack
    - Templates: [Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/) for server-side rendering
- Testing Frameworks
    - Unit Testing: [pytest](https://docs.pytest.org/) for Python testing
 
## Team Workflow

- **Team Members**: Calvin Arnold, Nathan Haustveit, Zach Johnston
- **Workflow**: Single repository with collaborators - all team members have full push/pull access to the main repository
- **Branch Strategy**: All team members commit directly to the main branch
- **Communication**: Team members coordinate changes through git commits with clear, descriptive messages
- **Testing**: Code changes are tested locally before being pushed to the repository
- **CI/CD**: The automated CI/CD pipeline runs all tests on every push to main to ensure code quality and catch issues early
