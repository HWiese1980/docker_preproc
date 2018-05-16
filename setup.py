#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name = "docker-preproc",
      version='1.0',
      description="preprocessor for dockerfiles",
      author='Hendrik Wiese',
      author_email='hendrik.wiese@dfki.de',
      packages=["dpp", "dpp"],
      entry_points = {
        'console_scripts': [
            "dpp = dpp.dpp:main"
        ]
      }
)
