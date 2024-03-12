#!/bin/bash

$ git config --global user.name "Nnamaka"
$ git config --global user.email "nnamaka7@gmail.com"

sudo apt-get update
sudo apt install nginx -y

# create python environment
sudo apt install python3-venv -y
python3 -m venv llm-env

# activate enviroment
source llm-env/bin/activate && pip install -r requirments.txt && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

