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

		try:
			config_path = os.path.join(self.cache_dir, 'homebrew_config.txt')
			if not os.path.exists(config_path):
				brew_config = subprocess.run(['brew', 'config'], capture_output=True)
				with open(config_path, 'w') as file:
					file.write(brew_config.stdout.decode('utf-8', 'ignore'))

			config = open(config_path, 'r').read()

			config_data = config.split('\n')
			for c in config_data:
				try:
					k, v = c.split(": ", 1)
				except ValueError:
					continue

				if k == 'HOMEBREW_VERSION':
					self.version = v
				if k == 'Core tap HEAD':
					self.core_tap_head = v
		except (FileNotFoundError, IndexError): # Homebrew isn't installed
			self.version = None
			self.core_tap_head = None

		self.update() # XXX Remove me

	def update(self):
		info_path = os.path.join(self.cache_dir, 'homebrew.json')
		if not os.path.exists(info_path):
			brew_info = subprocess.run(['brew', 'info', '--all', '--json'], capture_output=True)
			with open(info_path, 'w') as file:
				file.write(brew_info.stdout.decode('utf-8', 'ignore'))

		packages = json.load(open(info_path, 'r'))

		for package in packages:
			self._addpackage(HomebrewPackage.from_dictionary(package, self))

		# package_list = subprocess.run(['brew', 'search'], capture_output=True)

	def install(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def uninstall(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def upgrade(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def firstaid(self):
		raise AttributeError("Abstract method was not overwritten by child class")
