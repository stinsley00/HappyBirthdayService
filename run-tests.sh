# setup a python virtual env and set PYTHONPATH={pwd}

echo 'INSTALLING PYTHON REQs...'
python3 -m venv venv
export PYTHONPATH=$(pwd)

venv/bin/pip3 install -qqr requirements.txt -r test-requirements.txt
# venv/bin/pytest tests/test-sql.py
venv/bin/python -m unittest tests/test-email.py
