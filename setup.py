#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


dependencies = []
test_dependencies = ['django>1.4.0']

setup(
    name='django-stronghold',
    version='0.2.7',
    description='Get inside your stronghold and make all your Django views default login_required',
    url='https://github.com/mgrouchy/django-stronghold',
    author='Mike Grouchy',
    author_email="mgrouchy@gmail.com",
    packages=[
        'stronghold',
        'stronghold.tests',
    ],
    license='MIT license',
    install_requires=dependencies,
    tests_require=test_dependencies,
    long_description=open('README.rst').read(),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
)
