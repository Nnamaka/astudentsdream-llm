#!/bin/bash

sudo apt-get update
sudo apt install nginx -y

# create python environment
sudo apt install python3-venv
python3 -m venv llm-env


# activate enviroment
source llm-env/bin/activate

# install dep
pip install -r requirments.txt

exit 0
