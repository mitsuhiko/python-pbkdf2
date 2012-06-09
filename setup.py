import os
from setuptools import setup

readme = open(os.path.join(os.path.dirname(__file__), 'README'), 'r').read()

setup(
    name='pbkdf2',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version='1.0',
    url='http://github.com/mitsuhiko/python-pbkdf2',
    py_modules=['pbkdf2'],
    description='A simple and straightforward implementation of pbkdf2.  Also copy/pasteable',
    long_description=readme,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ]
)
