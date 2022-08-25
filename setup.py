#! /usr/bin/env python3
"""Install script."""

from setuptools import setup


setup(
    name='is24csv',
    use_scm_version={
        "local_scheme": "node-and-timestamp"
    },
    setup_requires=['setuptools_scm'],
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='info@homeinfo.de',
    maintainer='Richard Neumann',
    maintainer_email='r.neumann@homeinfo.de',
    packages=['is24csv'],
    description='Immobilienscout24 legacy CSV library.'
)
