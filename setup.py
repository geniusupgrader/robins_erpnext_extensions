# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in robins_erpnext_extensions/__init__.py
from robins_erpnext_extensions import __version__ as version

setup(
	name='robins_erpnext_extensions',
	version=version,
	description='Robins Erpnext Extensions',
	author='Robin Rosenstock',
	author_email='robin.rosenstock@t-online.de',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
