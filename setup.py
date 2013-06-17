#!/usr/bin/env python

from distutils.core import setup

setup(name='archinator',
      version='0.5.0',
      description='Virtual machine generator for ArchLinux',
      author='Thomas S Hatch',
      author_email='thatch45@gmail.com',
      url='https://github.com/thatch45/archinator',
      packages=[
          'archinator',
          'archinator.utils',
          ],
      scripts=['scripts/archinator'],
     )

