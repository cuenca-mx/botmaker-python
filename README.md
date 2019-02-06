# BotMaker client library

[![Build Status](https://travis-ci.com/cuenca-mx/botmaker-python.svg?branch=master)](https://travis-ci.com/cuenca-mx/botmaker-python)
[![Coverage Status](https://coveralls.io/repos/github/cuenca-mx/botmaker-python/badge.svg?branch=master)](https://coveralls.io/github/cuenca-mx/botmaker-python?branch=master)
[![PyPI](https://img.shields.io/pypi/v/botmaker.svg)](https://pypi.org/project/botmaker/)


## Installation

```bash
pip install botmaker
```

## Run tests

```bash
make venv
source venv/bin/activate
export BOTMAKER_ACCESS_TOKEN={access_token}
make test
```

## Release to PyPi

```bash
pip install -U setuptools wheel twine
make release
# PyPi will prompt you to log in
```

## Usage

### Send a message based on an existing template

```python
import botmaker


client = botmaker.Client()  # Will use the env var BOTMAKER_ACCESS_TOKEN

# Send from '5215500000000' to '5215522222222'
client.template_messages.create(
    '5215500000000', '5215522222222',
    'template_name', template_param1='x', template_param2='y'
)
```
