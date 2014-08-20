#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name='django-mailtemplates',
        version='0.3',
        description='django mail templates',
        maintainer='cuescience',
        maintainer_email='kontakt@cuescience.de',
        license="MIT",
        url='',
        packages=['mailtemplates'],
        install_requires=[
	       "Django",
         "requests"
	]
     )
