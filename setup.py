#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

long_description = readme

setup(
    name='runp3',
    version='0.0.1d',
    description='runp exports Python functions from files to the command line',
    long_description=long_description,
    author='Takashi Kusachi',
    author_email='aisiars@gmail.com',
    url='https://github.com/TakashiKusachi/runp',
    packages=find_packages(),
    test_suite='tests',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'runp = runp.runp:main',
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development'
    ],
    python_requires='>3.7.11',
)
