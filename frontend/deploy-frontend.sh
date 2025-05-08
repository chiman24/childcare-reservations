#!/bin/bash

EC2_USER="ec2-user"
EC2_IP=3.83.112.248
PEM_KEY="~/ec2-us-east-1-keypair.pem"
FRONTEND_BUILD_DIR="dist"
REMOTE_FRONTEND_DIR="/var/www/frontend"
BACKEND_PORT=8000

# Copy the frontend build to the EC2 instance
scp -o StrictHostKeyChecking=accept-new -i "$PEM_KEY" -r "$FRONTEND_BUILD_DIR/" "$EC2_USER@$EC2_IP:~"

# Move the frontend build to the remote frontend directory and restart Nginx
ssh -i "$PEM_KEY" "$EC2_USER@$EC2_IP" << EOF
    sudo rm -rf $REMOTE_FRONTEND_DIR
    sudo mkdir -p $REMOTE_FRONTEND_DIR
    sudo mv ~/$FRONTEND_BUILD_DIR/* $REMOTE_FRONTEND_DIR/
    sudo systemctl restart nginx
EOF

echo "Frontend deployed and Nginx restarted at http://$EC2_IP"