# Django CI/CD Project

## Overview
This is a simple Django application demonstrating a CI/CD pipeline using GitHub Actions. The app is containerized with Docker Compose, served via Nginx as a reverse proxy, and deployed to a Linode server. It’s accessible only via a configured domain (e.g., `https://cicd.infinitebitworks.xyz/`) with Cloudflare providing SSL/TLS and IP protection.

The homepage displays a styled "Welcome to Django CI/CD!" message with a gradient background and a button, built for testing the pipeline.

## Project Structure
- `app/`: Django application code, including the `index` view with styled HTML.
- `nginx/`: Nginx configuration (`default.conf`) for reverse proxy and domain-only access.
- `docker-compose.yml`: Defines services for Django (`web`) and Nginx.

## Prerequisites
- **Linode Server**: Ubuntu with Docker and Docker Compose installed.
- **GitHub Repository**: Stores the project code and CI/CD workflow.
- **Cloudflare**: Manages DNS, SSL, and IP protection for the domain.
- **GitHub Secrets**:
  - `SSH_HOST`: Server IP.
  - `SSH_USER`: Server username.
  - `SSH_PASSWORD`: Server SSH password (consider switching to SSH keys).

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shyambista123/django-hello-cicd.git
   cd django-hello-cicd
   ```

2. **Configure Cloudflare**:
   - Add your domain and set an `A` record to the server’s IP with **Proxy status: Proxied**.
   - Enable **Full (strict)** SSL/TLS and **Always Use HTTPS**.

3. **Server Setup**:
   - Ensure Docker and Docker Compose are installed:
     ```bash
     sudo apt-get install -y docker.io docker-compose-plugin
     sudo usermod -aG docker <username>
     ```
   - Set up SSH access for the CI/CD pipeline.
   - Clone the repository to `/home/<username>/django-hello-cicd`.

4. **Nginx Configuration**:
   - The `nginx/default.conf` restricts access to the domain and blocks IP requests:
     ```nginx
     server {
         listen 80 default_server;
         server_name _;
         return 444;
     }
     server {
         listen 80;
         server_name example.com www.example.com;
         location /static/ { alias /app/staticfiles/; }
         location / { proxy_pass http://web:8000; ... }
     }
     ```

## Running Locally
1. Build and run with Docker Compose:
   ```bash
   docker compose up -d --build
   ```
2. Access at `http://localhost:8000` (Nginx proxies to Django).

## CI/CD Pipeline
The pipeline is defined in `.github/workflows/ci-cd.yml`:
- Triggers on push to the `main` branch.
- Deploys to the Linode server using `appleboy/ssh-action`.
- Updates the repository, rebuilds, and restarts containers:
  ```bash
  cd /home/<username>/django-hello-cicd
  git fetch origin
  git reset --hard origin/main
  git pull origin main
  docker compose down
  docker compose up -d --build
  ```

## Deployment
1. Push changes to the `main` branch:
   ```bash
   git add .
   git commit -m "Update application"
   git push origin main
   ```
2. The workflow deploys to `https://yourdomain.com`.

## Accessing the Application
- **URL**: `https://yourdomain.com` (replace with your domain).
- **IP Access**: Blocked (returns `444` or Cloudflare error).
- Displays a styled page with a "Welcome to Django CI/CD!" message.
