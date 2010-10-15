#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='admin_langswitch',
    version='0.1.4',
    author='Piotr Kilczuk',
    author_email='p.kilczuk@neumea.pl',
    url='http://github.com/centralniak',
    description = 'Adds easy language switch in admin',
    packages=find_packages(),
    provides=['admin_langswitch'],
    include_package_data=True,
    #package_data={'cmsplugin': ['templates/*',]},
    classifiers=[
        'Framework :: Django',
        #'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
