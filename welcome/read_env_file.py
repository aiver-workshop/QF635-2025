"""
You should NEVER hardcode any sensitive information such as password in Python script.
A safer way to handle credential is saving them in a local file and load as environment variables.
There are more secure ways to manage secrets such as using Secret Manager service by cloud providers.
Students are encourage to explore further.

Use Notepad to create a "secrets.txt" file under home directory ~/vault to store <key>=<value> pairs, for example:
key=abc
secret=123

Note: If your computer is compromised, then potentially your secret files are exposed too.
"""

import os
from dotenv import load_dotenv

env_path = os.path.expanduser('~/vault/secrets.txt')

load_dotenv(dotenv_path=env_path)
my_username = os.getenv('key')
my_password = os.getenv('secret')

print(my_username)
print(my_password)
