# -*- coding: utf-8 -*-

# pkgmgmnt: pkgmanagers/homebrew.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

import subprocess

from config import Config

from .main import *

class Homebrew(PackageManager):
	def __init__(self, app_config):
		super().__init__(app_config)
		self.name = "Homebrew"

		try:
			brew_config = subprocess.run(['brew', 'config'], capture_output=True)
			config_data = brew_config.stdout.split(b'\n')
			for c in config_data:
				try:
					k, v = c.decode('utf-8', 'ignore').split(": ", 1)
				except ValueError:
					continue

				if k == 'HOMEBREW_VERSION':
					self.version = v
				if k == 'Core tap HEAD':
					self.core_tap_head = v
		except (FileNotFoundError, IndexError): # Homebrew isn't installed
			self.version = None
			self.core_tap_head = None

		print("Homebrew Version: {0}".format(self.version))
		print("Core Tap Head: {0}".format(self.core_tap_head))

		self.update()

	def update(self):
		# package_info = subprocess.run(['brew', 'info', '--all', '--json'], capture_output=True)

		# XXX This is pseudo-data for testing purposes.  Provide real data later.
		
		self._addpackage(Package(self, 'python', '3.7.3', '3.7.3'))
		self._addpackage(Package(self, 'ruby', '2.6.3', '2.5.5'))
		self._addpackage(Package(self, 'zsh', '5.7.1', ''))

	def install(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def uninstall(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def upgrade(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def firstaid(self):
		raise AttributeError("Abstract method was not overwritten by child class")
