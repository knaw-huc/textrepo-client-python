# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import textrepo

with open('README.md', encoding='utf8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf8') as f:
    license = f.read()

setup(
    name='textrepo',
    version=textrepo.__version__,
    description='client to access textrepo',
    long_description=readme,
    author='Bram Buitendijk',
    author_email='bram.buitendijk@di.huc.knaw.nl',
    url='https://github.com/knaw-huc/textrepo-client-python',
    license=license,
    packages=find_packages(exclude=('integrationtests', 'tests', 'docs', 'notebooks'))
)
