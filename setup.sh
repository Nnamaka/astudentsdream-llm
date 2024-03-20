#!/bin/bash

git config --global user.name "Nnamaka"
git config --global user.email "nnamaka7@gmail.com"

sudo apt-get update
sudo apt install nginx -y

# download ollama
curl -fsSL https://ollama.com/install.sh | sh

# create python environment
sudo apt install python3-venv -y
python3 -m venv llm-env

# activate python environment and install deps
source llm-env/bin/activate && pip install -r requirments.txt && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

