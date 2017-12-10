import os
import sys
import codecs
import favicon

from distutils.core import setup
from setuptools import setup, find_packages

version = favicon.__version__

setup(
    name='django-favicon-plus',
    version=version,
    url='https://github.com/arteria/django-favicon-plus/',
    packages=find_packages(),
    license='BSD License',
    description='Favicon app for django',
    long_description=codecs.open('README.md', encoding='utf-8').read(),
    install_requires=open('requirements.txt').read().split('\n'),
    author='arteria GMBH',
    include_package_data=True,
    author_email='arteria@arteria.ch',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False
)
