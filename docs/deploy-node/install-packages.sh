#!/bin/bash
# This script installs the necessary dependencies on an EC2 instance.
sudo apt-get update
# Start a python virtual environment (.venv)
# Note: Linux based systems use python heavily and a virtual environment protects the system's packages
sudo python -m venv app-env
# Opens and activates virtual environment (venv)
sudo source app-env/bin/activate
# Pip package installer (Should be in the venv)
sudo python -m ensurepip --upgrade
# Install Django
sudo python -m pip install Django

# Apparently this method shouldn't need a refresh
echo "Installation script completed."