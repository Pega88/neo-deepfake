#!/usr/bin/env bash
#echo "yeey"
#ls
#cd ..
#cd ..
#cd ..
#ls
cp ~/Development/crypto/neo/neo-python/neo/bin/settings/$1 ~/Development/crypto/neo/neo-python/neo/bin/custom_settings.py
cd ~/Development/crypto/neo/neo-python
source venv/bin/activate
python --version
echo "START"
np-prompt -p | cat
echo "END"
