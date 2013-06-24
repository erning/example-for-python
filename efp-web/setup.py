# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup

srcdir = os.path.dirname(__file__) + '/src'

setup (
    name = 'efp-web',
    version = '1.0.dev',

    package_dir = {'': 'src'},
    packages = find_packages('src'),

    entry_points = {
        'console_scripts':
            ['hello = efp.web.hello:main']
    },

    install_requires = [
        'efp-core',
        'Flask==0.10'
    ],
    setup_requires = [],
    tests_require = [],

    author = "erning",
    description = "Example for python",
    url = "https://github.com/erning/example-for-python"
)
