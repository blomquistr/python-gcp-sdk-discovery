#!/usr/bin/env bash

# This script is used to setup the environment for the project.
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
