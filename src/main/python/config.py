# -*- coding: utf-8 -*-

# pkgmgmnt: config.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

import os, sys

class Config():
	def __init__(self, program_name):
		self.PROGRAM_NAME = program_name

		if sys.platform == 'win32':
			self.GOOBORG_DATA_PATH = os.path.expandvars('%LOCALAPPDATA%\\Gooborg Studios\\')
		else:
			self.GOOBORG_DATA_PATH = os.path.expanduser(os.path.join('~', '.gooborg'))

		self.DATA_PATH = os.path.join(self.GOOBORG_DATA_PATH, self.PROGRAM_NAME)

		self.create_data_dir()

	def create_data_dir(self):
		if os.path.exists(self.DATA_PATH):
			return # Directory already created

		if not os.path.exists(self.GOOBORG_DATA_PATH):
			os.mkdir(self.GOOBORG_DATA_PATH)
			# XXX Create little readme.txt here later on

		os.mkdir(self.DATA_PATH)
