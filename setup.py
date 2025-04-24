#!/usr/bin/env python3

from setuptools import setup

setup(
    name='bin_utils',
    version='0.0.1',
    install_requires=[],
    description='Command line helper.',
    url='https://github.com/fractal13/bin-utils',
    entry_points = {
        'console_scripts': ['random-order=bin_utils.random_order:cli'],
    },
)
