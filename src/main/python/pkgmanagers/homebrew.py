# -*- coding: utf-8 -*-

# pkgmgmnt: pkgmanagers/homebrew.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

from .main import *

class Homebrew(PackageManager):
	def __init__(self):
		super().__init__()
		self.name = "Homebrew"

		self.update()

	def update(self):
		# XXX This is pseudo-data for testing purposes.  Provide real data later.
		
		self._addpackage(Package(self, 'python', '3.7.3', '3.7.3'))
		self._addpackage(Package(self, 'ruby', '2.5.5', '2.6.3'))
		self._addpackage(Package(self, 'zsh', '', '5.7.1'))

	def install(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def uninstall(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def upgrade(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def firstaid(self):
		raise AttributeError("Abstract method was not overwritten by child class")
