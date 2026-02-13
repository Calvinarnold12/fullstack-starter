# Full-Stack Web Application

This repository contains a full-stack web application built with Node.js,
Express, and SQLite. It includes scripts and documentation for setting up,
configuring, and deploying the application on an AWS EC2 instance.

- [Development Guide](dev-node/README.md)
- [Deployment Guide (Docker)](deploy-docker/README.md)
- [Deployment Guide (Manual)](deploy-node/README.md)

## Technology Stack

- Backend technology stack
    - Web Server: [nginx](https://www.nginx.com/) as a reverse proxy server
    - Backend Runtime: [Node.js](https://nodejs.org/)
    - Backend Framework: [Express](https://expressjs.com/)
    - Database: [SQLite](https://www.sqlite.org/index.html) for lightweight data storage
- Frontend technology stack
    - Templates: [EJS](https://ejs.co/) for server-side rendering
    - UX/UI: [Bootstrap](https://getbootstrap.com/) for responsive design
- Testing Frameworks
    - End-to-End Testing: [Playwright](https://playwright.dev/)
 
## Team Workflow

- **Team Members**: Calvin Arnold, Nathan Haustveit, Zach Johnston
- **Workflow**: Single repository with collaborators - all team members have full push/pull access to the main repository
- **Branch Strategy**: All team members commit directly to the main branch
- **Communication**: Team members coordinate changes through git commits with clear, descriptive messages
- **Testing**: Code changes are tested locally before being pushed to the repository
- **CI/CD**: The automated CI/CD pipeline runs all tests on every push to main to ensure code quality and catch issues early
