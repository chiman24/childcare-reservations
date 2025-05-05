#!/bin/bash

# --- CONFIG ---
EC2_USER="ec2-user"
EC2_IP=3.83.112.248
PEM_KEY="~/ec2-us-east-1-keypair.pem"
FRONTEND_BUILD_DIR="dist"
REMOTE_FRONTEND_DIR="/var/www/frontend"
NGINX_CONF_LOCAL="frontend.conf"
NGINX_CONF_REMOTE="/etc/nginx/conf.d/frontend.conf"
BACKEND_PORT=8000
# --- END CONFIG ---

echo "Copying frontend build to EC2..."
scp -o StrictHostKeyChecking=accept-new -i "$PEM_KEY" -r "$FRONTEND_BUILD_DIR/" "$EC2_USER@$EC2_IP:~"

echo "Generating Nginx config..."
cat <<EOF > $NGINX_CONF_LOCAL

#server {
#    listen 80;
#    server_name jv.tools.childcare-reservations.big-heart-ventures.com;
#
#    return 301 https://\$host\$request_uri;
#}

server {
    listen 80;
    server_name jv.tools.childcare-reservations.big-heart-ventures.com;


    root $REMOTE_FRONTEND_DIR;
    index index.html;

    location / {
        try_files \$uri /index.html;
    }

    location /api/ {
        proxy_pass http://localhost:$BACKEND_PORT/api/;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

echo "Copying Nginx config to EC2..."
scp -i "$PEM_KEY" "$NGINX_CONF_LOCAL" "$EC2_USER@$EC2_IP:/tmp/frontend.conf"

echo "Moving Nginx config into place and restarting Nginx..."
ssh -i "$PEM_KEY" "$EC2_USER@$EC2_IP" << EOF
    sudo mv /tmp/frontend.conf $NGINX_CONF_REMOTE
    sudo mv ~/$FRONTEND_BUILD_DIR/* $REMOTE_FRONTEND_DIR/
    sudo nginx -t && sudo systemctl restart nginx
EOF

echo "Frontend deployed and Nginx restarted at http://$EC2_IP"
