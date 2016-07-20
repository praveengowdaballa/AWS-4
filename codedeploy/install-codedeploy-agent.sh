#!/bin/bash -ex
yum install -y aws-cli
cd /home/ec2-user/
wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/codedeploy-agent.noarch.rpm
yum -y install codedeploy-agent.noarch.rpm
service codedeploy-agent start