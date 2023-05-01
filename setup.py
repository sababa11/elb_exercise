"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='elb_exercise',
    version='0.1',
    description='cloud package',
    long_description=long_description,

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['Flask==2.3.2']

)
