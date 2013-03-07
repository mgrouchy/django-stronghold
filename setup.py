#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


dependencies = []
test_dependencies = ['django>1.3.1']

setup(
    name='django-stronghold',
    version='0.0.8',
    description='Get inside your stronghold and make all your Django views default login_required',
    url='https://github.com/mgrouchy/django-stronghold',
    author='Mike Grouchy',
    author_email="mgrouchy@gmail.com",
    packages=[
        'stronghold',
    ],
    license='MIT license',
    install_requires=dependencies,
    tests_require=test_dependencies,
    long_description=open('README.md').read(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)
