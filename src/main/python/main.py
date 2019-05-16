# -*- coding: utf-8 -*-

# pkgmgmnt: main.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

import sys

from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import qApp, QMainWindow, QWidget, QHBoxLayout, QAction, QComboBox, QLineEdit, QListWidget, QTableView
from PyQt5.QtGui import QIcon

appctxt = ApplicationContext()

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.resize(400, 300)
		self.setWindowTitle('Package Manager - Gooborg Studios')

		self.statusbar = self.statusBar()
		self.statusbar.showMessage('Initialized!')

		self.toolbar = self.initToolbar()

		self.widget = QWidget()
		self.setCentralWidget(self.widget)
		self.layout = QHBoxLayout()
		self.widget.setLayout(self.layout)

		self.filters = self.initFilters()
		self.layout.addWidget(self.filters, 1)

		self.packageGrid = self.initPackageGrid()
		self.layout.addWidget(self.packageGrid, 2)

		self.show()

	def initToolbar(self):
		toolbar = self.addToolBar('')

		exitAct = QAction(QIcon('./src/main/icons/base/32.png'), 'Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(qApp.quit)
		toolbar.addAction(exitAct)

		toolbar.addSeparator()

		combo = QComboBox()
		toolbar.addWidget(combo)
		combo.insertItems(1, ["Homebrew", "Pip", "Apt"])

		search = QLineEdit()
		toolbar.addWidget(search)
		search.setMaximumWidth(120)

		return toolbar

	def initFilters(self):
		filters = QListWidget()

		filters.addItem("All")
		filters.addItem("Installed")
		filters.addItem("Not Installed")
		filters.addItem("To Update")

		return filters

	def initPackageGrid(self):
		packageGrid = QTableView()

		return packageGrid



window = MainWindow()
exit_code = appctxt.app.exec_()
sys.exit(exit_code)
