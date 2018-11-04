#!/usr/bin/env bash
echo "yeey"
ls
cd ..
ls
python --version
cd neo-python
source venv/bin/activate
python --version
echo "START"
np-prompt -p | cat
echo "END"