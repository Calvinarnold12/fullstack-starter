#!/bin/bash
# This script installs the necessary dependencies on an EC2 instance.
sudo apt-get update
#Install venv
sudo apt install python3.12-venv
# Start a python virtual environment (.venv)
# Note: Linux based systems use python heavily and a virtual environment protects the system's packages
sudo python3 -m venv app-env
sudo echo "$(ls -l)"
# Opens and activates virtual environment (venv)
sudo bash source app-env/bin/activate
# Pip package installer (Should be in the venv)
sudo python3 -m ensurepip --upgrade
# Install Django
sudo python3 -m pip install Django

# Apparently this method shouldn't need a refresh
echo "Installation script completed."