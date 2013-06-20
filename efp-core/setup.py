# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup

srcdir = os.path.dirname(__file__) + '/src'

setup (
    name = 'efp-core',
    version = '1.0.dev',

    package_dir = {'': srcdir},
    packages = find_packages(srcdir),

    install_requires = [],
    setup_requires = [],
    tests_require = [],

    author = "erning",
    description = "Example for python",
    url = "https://github.com/erning/example-for-python"
)
