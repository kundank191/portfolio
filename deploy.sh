#!/bin/bash

# This script automates Docker installation and deployment for Python app in production

# Update the system and install prerequisites
echo "Updating system packages..."
sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing dependencies..."
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# Install Docker
echo "Installing Docker..."
curl -fsSL https://get.docker.com | sudo bash

# Enable Docker to start on boot
sudo systemctl enable docker
sudo systemctl start docker

# Install Docker Compose
echo "Installing Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify Docker installation
echo "Verifying Docker installation..."
docker --version
docker-compose --version

# Navigate to your project directory (replace with your project path)
echo "Navigating to the project directory..."
cd /home/ubuntu/portfolio || exit

# Build and run the Docker container
echo "Building and running Docker container..."
sudo docker-compose up --build -d

# Install Nginx for reverse proxy
echo "Installing Nginx..."
sudo apt-get install -y nginx

# Configure Nginx as a reverse proxy to the Docker container
echo "Configuring Nginx..."
sudo cat > /etc/nginx/sites-available/myapp <<EOF
server {
    listen 80;
    server_name your-ec2-ip;

    location / {
        proxy_pass http://127.0.0.1:80;  # Proxy to Gunicorn running on port 80 inside the container
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Enable the Nginx configuration and restart the service
echo "Enabling Nginx configuration and restarting..."
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
sudo systemctl restart nginx

# Allow Nginx to restart automatically on EC2 boot
sudo systemctl enable nginx

# Enable Docker to restart on boot
sudo systemctl enable docker

# Test if everything is working fine
echo "Deployment successful! You can now access your app at http://your-ec2-ip:5000"

# End of script
EOF