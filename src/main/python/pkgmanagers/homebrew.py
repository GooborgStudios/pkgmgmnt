# -*- coding: utf-8 -*-

# pkgmgmnt: pkgmanagers/homebrew.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

import subprocess, os, json

from config import Config

from .main import *

class HomebrewPackage(Package):
	@classmethod
	def from_dictionary(cls, dictionary, manager):
		version = ''
		installed = dictionary['installed']
		if installed:
			version = installed[0]['version']

		self = cls(manager, dictionary['name'], dictionary['versions']['stable'], version)
		return self

class Homebrew(PackageManager):
	def __init__(self, app_config):
		super().__init__("Homebrew", app_config)

		self.cache_dir = self.app_config.create_data_dir(self.name)

		self._config_path = os.path.join(self.cache_dir, 'homebrew_config.txt')
		self._info_path = os.path.join(self.cache_dir, 'homebrew.json')
		self._list_path = os.path.join(self.cache_dir, 'homebrew_list.txt')
		
		self.update() # XXX Remove me

	def _parse_config(self, config_string):
		# take the  raw 'brew config' data
		# return a dictionary of important config vars
		config_data = config_string.split('\n')
		config = {}
		for c in config_data:
			try:
				k, v = c.split(": ", 1)
			except ValueError:
				continue

			if k == 'HOMEBREW_VERSION':
				config['version'] = v
			if k == 'Core tap HEAD':
				config['core_tap_head'] = v
		return config

	def _parse_list(self, list_string):
		# take the raw 'brew list' data 
		# return a package:version dictionary
		pass

	def _update_config(self):
		# Read the Homebrew config
		# Check against cached config
		# Has core tap HEAD changed?

		try:
			if os.path.exists(self._config_path):
				old_config = self._parse_config(self._config_path)
			else:
				old_config = None

			brew_config = subprocess.run(['brew', 'config'], capture_output=True)
			with open(self._config_path, 'w') as file:
				file.write(brew_config.stdout.decode('utf-8', 'ignore'))
			new_config = self._parse_config(open(self._config_path, 'r').read())

			if not old_config or new_config['core_tap_head'] != old_config['core_tap_head']:
				self._update_info()
				pass

		except (FileNotFoundError, IndexError): # Homebrew isn't installed
			self.version = None
			self.core_tap_head = None


	def _update_info(self):
		if not os.path.exists(self._info_path):
			brew_info = subprocess.run(['brew', 'info', '--all', '--json'], capture_output=True)
			with open(info_path, 'w') as file:
				file.write(brew_info.stdout.decode('utf-8', 'ignore'))


	def _update_installed(self):
		old_list = self._parse_list(self._list_path)
		brew_list = subprocess.run(['brew', 'list'], capture_output=True)
		with open(self._list_path, 'w') as file:
			file.write(brew_list.stdout.decode('utf-8', 'ignore'))
		new_list = self._parse_config(open(self._list_path, 'r').read())

		for pkg in new_list:
			if pkg in old_list:
				del old_list[pkg]
			pkg_info = subprocess.run(['brew', 'info', '--json', pkg], capture_output=True)

		# XXX mark anything left in old list as uninstalled

	def update(self):
		self._update_config()

		packages = json.load(open(self._info_path, 'r'))

		for package in packages:
			self._addpackage(HomebrewPackage.from_dictionary(package, self))

		self._update_installed()

		# package_list = subprocess.run(['brew', 'search'], capture_output=True)

	
		# Obtain new Homebrew info --all
	# No?
		# Read Homebrew list
		# Check against cached list
		# Any new or removed packages?
			# Mark as such within JSON database
		# Check each installed package for installed version

	# When a new package is installed, update the cached info JSON

	def install(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def uninstall(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def upgrade(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def firstaid(self):
		raise AttributeError("Abstract method was not overwritten by child class")
