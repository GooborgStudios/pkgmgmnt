# -*- coding: utf-8 -*-

# pkgmgmnt: pkgclass.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

class Package:
	def __init__(self, manager, name, version):
		self.name = name
		self.version = version
		self.manager = manager
		self.dependencies = []
		self.description = ""
		self.url = ""
