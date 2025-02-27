#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup envvars
"""

import dotenv

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='python-env',
    version=dotenv.__version__,
    description='Get and Set environment variables using .env file',
    author='Matt Seymour',
    author_email='mattaseymour@gmail.com',
    url="http://github.com/mattseymour/python-env",
    packages=['dotenv'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    test_suite='tests'
)
