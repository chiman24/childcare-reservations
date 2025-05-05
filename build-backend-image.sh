#!/bin/zsh

#Build image
docker build -t 721020354128.dkr.ecr.us-east-1.amazonaws.com/big-heart-tech/jv-childcare-reservations-repo:$1 backend/

#Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 721020354128.dkr.ecr.us-east-1.amazonaws.com

#Push image to ECR repo
docker push 721020354128.dkr.ecr.us-east-1.amazonaws.com/big-heart-tech/jv-childcare-reservations-repo:$1