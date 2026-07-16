# Flask CI/CD Pipeline with GitHub Actions & Docker

#### This project demonstrates a basic CI/CD pipeline for deploying a Dockerized Flask application to a VPS using GitHub Actions.

```
GitHub
   │
   │ git push
   ▼
GitHub Actions
   │
   │ SSH
   ▼
Your VPS
   │
   ├── git pull
   ├── docker compose build
   ├── docker compose up -d
   ▼
Flask container running
```

