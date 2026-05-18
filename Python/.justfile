test:
    ./venv/bin/python -m pytest

install:
    virtualenv venv
    ./venv/bin/pip install -r requirements.txt
