# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():  # Remove the 'package' argument
    """Return package version."""
    init_py = open(os.path.join(os.path.dirname(__file__), '__init__.py')).read()
    return re.search(r"^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)

setup(
    name='pyboleto',
    version=get_version(),
    author='Caio Sousa',
    author_email='caio.sousa@upp.com.br',
    url='https://github.com/caiosousaupp/python3-boleto',
    packages=find_packages(),
    package_dir={'': '.'},
    package_data={
        '': ['LICENSE'],
        'pyboleto': ['media/*.jpg', 'media/*.png', 'templates/*.html'],
        'tests': ['xml/*.xml']
    },
    zip_safe=False,
    provides=[
        'pyboleto'
    ],
    license='BSD',
    description='Python Library to create "boletos de cobrança bancária" for \
    several Brazilian banks',
    long_description=read('README.rst'),
    download_url='http://pypi.python.org/pypi/pyboleto',
    scripts=[
        os.path.join(os.path.pardir, 'bin', 'html_pyboleto_sample.py'),
        os.path.join(os.path.pardir, 'bin', 'pdf_pyboleto_sample.py'),
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Portuguese (Brazilian)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
    ],
    platforms='any',
    test_suite='tests.alltests.suite',
    install_requires=[
        'reportlab'
    ],
    tests_require=[
        'pylint',
        'tox',
        'coverage',
        'pep8',
        'sphinx-pypi-upload',
        'sphinx'
    ]
)
