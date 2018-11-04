#!/usr/bin/env bash
echo "yeey"
ls
cd ..
ls
python --version
cd neo-python
source venv/bin/activate
python --version
#python ../flask-server/fake_tty.py
echo "START"
np-prompt -p | cat
echo "END"