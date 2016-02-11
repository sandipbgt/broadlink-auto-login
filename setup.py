#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
requirements = [pkg.split('=')[0] for pkg in open('requirements.txt').readlines()]

description = "Broadlink hotspot auto login script"

long_description = open("README.rst").read()

classifiers = ['Environment :: Console',
               'Programming Language :: Python :: 3'
               ]

version = open('CHANGES.txt').readlines()[0][1:].strip()

setup(name='broadlink-auto-login',
      version=version,
      description=description,
      author='Sandip Bhagat',
      author_email='sandipbgt@gmail.com',
      url='https://github.com/sandipbgt/broadlink-auto-login',
      scripts=['src/broadlink',],
      install_requires=requirements,
      long_description=long_description,
      packages=['broadlink_auto_login'],
      package_dir = {'broadlink_auto_login': 'src/broadlink_auto_login'},
      classifiers=classifiers
    )