# -*- coding: utf-8 -*-

# pkgmgmnt: pkgmanagers/homebrew.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

from .main import *

class Homebrew(PackageManager):
	def __init__(self):
		self.name = "Homebrew"

	def update():
		raise AttributeError("Abstract method was not overwritten by child class")

	def install(pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def uninstall(pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def upgrade(pkg):
		raise AttributeError("Abstract method was not overwritten by child class")

	def firstaid():
		raise AttributeError("Abstract method was not overwritten by child class")