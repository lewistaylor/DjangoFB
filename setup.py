#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='djangoFB',
      version='0.01',
      description='Utility suite for Facebook',
      author='Captain Awesome',
      author_email='lewisctaylor@gmail.com',
      url='git://github.com/lewistaylor/DjangoFB.git',
      packages=['fb'],
      test_suite='fb.tests',
      tests_require=[''])
