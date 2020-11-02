from distutils.core import setup
from pathlib import Path


exec(open("mediatr/_version.py", encoding="utf-8").read())

setup(
  name = 'mediatr', 
  packages = ['mediatr'],  
  version = __version__,     
  license="MIT -or- Apache License 2.0",
#   long_description=Path(__file__).with_name("README.md").read_text('utf-8'),
  description="mediator pattern and CQRS implementation with pipline behaviors for Python 3.5+",
  author = 'Evgeniy Fetisov',               
  author_email = 'me@efetisov.ru',  
  url = 'https://github.com/megafetis/mediatr_py',
  keywords = ['mediator','mediatr', 'CQRS','cqrs','pipline', 'behaviors', 'command', 'query', 'responsability', 'segregation','command bus','bus' ], 
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