#!/bin/bash

# remove this git configuration later
# REMOVE: 1
git config --global user.name "Nnamaka"
git config --global user.email "nnamaka7@gmail.com"

sudo apt-get update
sudo apt install nginx -y

# download ollama
curl -fsSL https://ollama.com/install.sh | sh

# download gemma 2:2b
ollama pull gemma:2b

# create python environment and activate environment
# REMOVE: 2
sudo apt install python3-venv -y
python3 -m venv llm-env
source llm-env/bin/activate

# install deps
pip install -r requirments.txt && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# install redis
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis -y

