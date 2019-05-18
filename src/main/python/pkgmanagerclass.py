# -*- coding: utf-8 -*-

# pkgmgmnt: pkgmanagerclass.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

class PackageManager:
	"""
	The PackageManager class is an abstract class to be overwritten by a child class, containing all the basic variables and methods.
	"""
	def __init__(self):
		self.name = "ABSTRACT" # To be overwritten by child
		self.packages = {}

	def update():
		"""
		This function updates the list of packages, as well as the package manager if needed.
		"""
		raise AttributeError("Abstract method was not overwritten by child class")

	def install(pkg):
		"""
		This function installs a specified package, including all of its dependencies, if not already installed.
		"""
		raise AttributeError("Abstract method was not overwritten by child class")

	def uninstall(pkg):
		"""
		This function uninstalls a specified package if it's installed.
		"""
		raise AttributeError("Abstract method was not overwritten by child class")

	def upgrade(pkg):
		"""
		This function upgrades a specified package if it's installed, including dependencies if needed.
		"""
		raise AttributeError("Abstract method was not overwritten by child class")

	def firstaid():
		"""
		This function includes a series of commands to perform basic cleanup and fix common issues within the package manager.
		"""
		raise AttributeError("Abstract method was not overwritten by child class")
