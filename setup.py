#!/usr/bin/env python

from distutils.core import setup
import platform

def build_params():
    params = {
      'name':'copycat-clipboard3',
      'version':'1.0',
      'description':'easy way let use clip on command line with system clip (support python 3)',
      'author':'Ming',
      'author_email':'ming@alone.tw',
      'url':'https://github.com/iwdmb/copycat',
      'py_modules':['copycat'],
	  'license':'MIT',
      'install_requires': ['clime', 'pyclip-copycat'],
    }
    if platform.system() == 'Windows':
        params['scripts'] = ['copycat.bat']
    else:
        params['scripts'] = ['copycat']

    return params

setup(
    **build_params()
)
