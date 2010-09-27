#!/usr/bin/env python

from distutils.core import setup

setup(
    name='admin_langswitch',
    version='0.1.1',
    author='Piotr Kilczuk',
    author_email='p.kilczuk@neumea.pl',
    url='http://github.com/centralniak',
    description = 'Adds easy language switch in admin',
    packages = ['admin_langswitch',],
    package_data={'cmsplugin': ['templates/*',]},
)
