# -*- coding: utf-8 -*-

# pkgmgmnt: pkgmanagers/main.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

class PackageManager:
	"""
	The PackageManager class is an abstract class to be overwritten by a child class, containing all the basic variables and methods.
	"""
	def __init__(self):
		self.name = "ABSTRACT" # To be overwritten by child
		self.packages = {}

	def update(self):
		"""
		This function updates the list of packages, as well as the package manager if needed.
		"""
		raise AttributeError("Abstract method was not overwritten by child class")

	def install(self, pkg):
		"""
		This function installs a specified package, including all of its dependencies, if not already installed.
		"""
		raise AttributeError("Abstract method was not overwritten by child class")

	def uninstall(self, pkg):
		"""
		This function uninstalls a specified package if it's installed.
		"""
		raise AttributeError("Abstract method was not overwritten by child class")

	def upgrade(self, pkg):
		"""
		This function upgrades a specified package if it's installed, including dependencies if needed.
		"""
		raise AttributeError("Abstract method was not overwritten by child class")

	def firstaid(self):
		"""
		This function includes a series of commands to perform basic cleanup and fix common issues within the package manager.
		"""
		raise AttributeError("Abstract method was not overwritten by child class")

class Package:
	def __init__(self, manager, name, version):
		self.name = name
		self.version = version
		self.manager = manager
		self.dependencies = []
		self.description = ""
		self.url = ""
