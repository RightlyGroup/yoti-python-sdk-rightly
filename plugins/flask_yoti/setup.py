# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

VERSION = '0.1.0'
long_description = 'Long description'

setup(
    name='flask_yoti',
    version=VERSION,
    packages=find_packages(),
    license='MIT',
    description='Yoti Flask plugin for back-end integration.',
    long_description=long_description,
    url='https://github.com/lampkicking/yoti-sdk-server-python/plugins/flask_yoti',
    author='',
    author_email='',
    install_requires=['flask>=0.10', 'yoti>=0.1.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='',
)
