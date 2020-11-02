# from distutils.core import setup
from pathlib import Path
from setuptools import setup

exec(open("mediatr/_version.py", encoding="utf-8").read())

from os import path
this_directory = path.abspath(path.dirname(__file__))

long_description=None

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
  name = 'mediatr', 
  packages = ['mediatr'],  
  version = __version__,     
  license="MIT -or- Apache License 2.0",
  description="mediator and CQRS pattern implementation with pipline behaviors for Python 3.5+. Mediatr py",
  long_description_content_type='text/markdown',
  long_description=long_description,
  author = 'Evgeniy Fetisov',               
  author_email = 'me@efetisov.ru',  
  url = 'https://github.com/megafetis/mediatr_py',
  keywords = ['mediator','mediatr', 'CQRS','cqrs','mediatr_py','mediator py','mediatr py','pipline', 'behaviors', 'command', 'query', 'responsability', 'segregation','command bus','bus' ], 
  python_requires=">=3.5",
  
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    "License :: OSI Approved :: MIT License",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
  ],
)