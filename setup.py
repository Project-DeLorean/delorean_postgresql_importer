#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

from version import __version__


dependencies = ['click']

setup(
    name='delorean_postgresql_importer',
    version=__version__,
    description='Library to import ESRI Shapefiles \
    into a PostgreSQL database.',
    url='https://github.com/Project-DeLorean/delorean_postgresql_importer',
    author='Tobias Preuss',
    author_email="tobias.preuss@googlemail.com",
    packages=[
        'delorean_postgresql_importer',
    ],
    license='AGPLv3+',
    install_requires=dependencies,
    long_description=open('README.rst').read(),
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: \
        GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'console_scripts': [
            'delorean_postgresql_importer = \
            delorean_postgresql_importer.cli:import_shapefiles'
        ]
    },
)
