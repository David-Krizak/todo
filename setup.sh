#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "Gotovo."
echo "Pokreni aplikaciju s:"
echo "source venv/bin/activate"
echo "python app.py"
