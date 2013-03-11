# -*- coding: utf-8 -*-
# Copyright (C) 2012 Ludia Inc.
# This software is licensed as described in the file LICENSE, which
# you should have received as part of this distribution.
# Author: Pior Bastida <pbastida@socialludia.com>

from setuptools import setup, find_packages
import codecs

version = '0.4.dev0'


def read(filename):
    return unicode(codecs.open(filename, encoding='utf-8').read())

long_description = '\n\n'.join([read('README.rst'),
                                read('CREDITS.rst'),
                                read('CHANGES.rst')])

setup(name='awstools',
      version=version,
      description="High level tools to manage an AWS infrastructure",
      long_description=long_description,
      classifiers=[
          "Intended Audience :: System Administrators",
          "Environment :: Console",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
      ],
      keywords='',
      author='Pior Bastida',
      author_email='pior@pabstida.net',
      url='https://bitbucket.org/pior/awstools',
      license='GPL',
      packages=find_packages(exclude=["awstools.costreport"]),
      # include_package_data=True,
      zip_safe=False,
      install_requires=[
          "argh",
          "PyYaml",
          "boto",
      ],
      extras_require={
          'test': ['nose', 'nosexcover', 'coverage', 'mock']
      },
      entry_points={},
      scripts=[
          "scripts/cfn",
          "scripts/ec2ssh",
      ]
      )
