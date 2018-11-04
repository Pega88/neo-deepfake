#!/usr/bin/env bash
#echo "yeey"
#ls
#cd ..
#cd ..
#cd ..
#ls
mv settings.py ~/Development/crypto/neo/neo-python/neo/bin/
cd ~/Development/crypto/neo/neo-python
source venv/bin/activate
python --version
echo "START"
np-prompt -p | cat
echo "END"
