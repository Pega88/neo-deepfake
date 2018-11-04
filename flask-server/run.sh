#!/usr/bin/env bash
#echo "yeey"
#ls
#cd ..
#cd ..
#cd ..
#ls
mv settings.py ~/Development/zurich/new-local-neo-python/neo-python/neo/bin/
cd ~/Development/zurich/new-local-neo-python/neo-python
source venv/bin/activate
python --version
echo "START"
np-prompt -p | cat
echo "END"
