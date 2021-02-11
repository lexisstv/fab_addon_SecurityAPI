import os
import sys
import imp
import multiprocessing
from setuptools import setup, find_packages

addon = imp.load_source('config', 'config.py')
version = imp.load_source('version', os.path.join(addon.FULL_ADDON_NAME, 'version.py'))

def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def read(fname):
    return open(fpath(fname)).read()

def desc():
    return read('README.md')

setup(
    name=addon.FULL_ADDON_NAME,
    version=version.VERSION_STRING,
    url='https://github.com/lexisstv/fab_addon_SecurityAPI/',
    license='BSD',
    author=version.AUTHOR_NAME,
    author_email=version.AUTHOR_EMAIL,
    description=version.DESCRIPTION,
    long_description=desc(),
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask-AppBuilder>=3.1.1',
    ],
    tests_require=[
        'nose>=1.0',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='nose.collector'
)
