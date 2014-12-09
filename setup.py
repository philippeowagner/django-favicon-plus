import os
import sys
import favicon

from distutils.core import setup
from setuptools import setup, find_packages

version = favicon.__version__

setup(
    name='django-favicon-plus',
    version=version,
    packages=find_packages(),
    license='BSD',
    description='Favicon app for django',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().split('\n'),
    author='arteria GMBH',
    include_package_data=True,
    author_email='arteria@arteria.ch',
)
