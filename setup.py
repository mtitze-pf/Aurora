'''
Setup for Aurora package. Basic call (install in editable mode)
pip install -e .

To install with a different Fortran compiler, use e.g.
python3 setup.py build --fcompiler=gnu95
or
python3 setup.py build --fcompiler=intelem 

It should be possible to pass any f2py flags via the command line, e.g. using
python3 setup.py build --fcompiler=intelem --opt="-fast"

'''

import setuptools
import os, sys, subprocess
from numpy.distutils.core import setup, Extension
from numpy.distutils.misc_util import Configuration

package_name='aurorafusion'

with open('README.md', 'r') as fh:
    long_description = fh.read()

wrapper = Extension(name='aurora._aurora', 
                    sources=['aurora/main.f90',
                             'aurora/grids.f90',
                             'aurora/impden.f90',
                             'aurora/math.f90'])

aurora_dir = os.path.dirname(os.path.abspath(__file__))
install_requires = open('requirements.txt').read().split('\n')
    
config = Configuration(
      name=package_name,
      description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/fsciortino/Aurora',
      author='F. Sciortino',
      author_email='sciortino@psfc.mit.edu',
      packages=['aurora'], #setuptools.find_packages(),
      setup_requires=["numpy"],
      install_requires=install_requires,
      ext_modules=[wrapper],
      classifiers=['Programming Language :: Python :: 3',
                   'Operating System :: OS Independent',
                   ],
      )
setup(**config.todict())
