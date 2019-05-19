# -*- coding: utf-8 -*-

# pkgmgmnt: pkgmanagers/homebrew.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

from .main import *

class Homebrew(PackageManager):
	def __init__(self):
		self.name = "Homebrew"

	def update(self):
		raise AttributeError("Abstract method was not overwritten by child class")

	def install(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def uninstall(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def upgrade(self, pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def firstaid(self):
		raise AttributeError("Abstract method was not overwritten by child class")