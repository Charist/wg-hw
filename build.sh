#!/bin/bash

# sudo easy_install virtualenv

if [ ! -d venv ]; then
    virtualenv -p $(which python3.4) venv
fi


source venv/bin/activate
pip install -r requirements.txt