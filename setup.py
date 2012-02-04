import hoiio

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

required = ['requests >= 0.10.2',]
packages = [
    'hoiio',
    'hoiio.rest',
    'hoiio.rest.resources',
]

setup(
    name='python-hoiio',    
    version=hoiio.__version__,
    description='A python module for Hoiio REST API',

    author='Mickey Cheong',
    author_email='mickeyckm@gmail.com',
    url='https://github.com/mickeyckm/python-hoiio',
    
    packages=packages,
    install_requires=required,    
    
    classifiers = [
         'Programming Language :: Python :: 2',
   ],
)