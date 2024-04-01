#!/bin/bash

# remove this git configuration later
# REMOVE: 1
git config --global user.name "Nnamaka"
git config --global user.email "nnamaka7@gmail.com"


# setup ec2 for nginx server and some deps
sudo apt-get update
sudo apt install nginx -y

cd /etc/nginx/sites-enabled/ 

public_ip=$(curl -s ifconfig.me)
text="server {
  listen 80;
  server_name <public ip address>;
  location / {
    proxy_pass http://127.0.0.1:8000;
  }
}"

sudo tee servellm_nginx <<< "$text" >/dev/null 2>&1

sudo sed -i "s/<public ip address>/$public_ip/" servellm_nginx

sudo rm default
sudo sudo service nginx restart && cd ~/astudentsdream-llm/

# download ollama
curl -fsSL https://ollama.com/install.sh | sh
(sudo ollama pull gemma:2b)

# create python environment and activate environment
# REMOVE: 2
sudo apt install python3-venv -y
python3 -m venv llm-env
source llm-env/bin/activate

# install deps
pip install -r requirments.txt && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# install redis
curl -fsSL https://packages.redis.io/gpg | sudo gpg -f --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis -y


echo "✅LLM server is now running on your public IP address: $public_ip"