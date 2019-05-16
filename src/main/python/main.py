# -*- coding: utf-8 -*-

# pkgmgmnt: main.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

import sys

from fbs_runtime.application_context import ApplicationContext
from PyQt5 import QtCore
from PyQt5 import QtWidgets as Qt
from PyQt5.QtGui import QIcon

appctxt = ApplicationContext()

class MainWindow(Qt.QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setUnifiedTitleAndToolBarOnMac(True)
		self.setWindowTitle('Package Manager - Gooborg Studios')

		self.resize(1024, 768)

		self.toolbar = self.initToolbar()
		self.statusbar = self.initStatusbar()

		self.widget = Qt.QWidget()
		self.setCentralWidget(self.widget)
		self.layout = Qt.QHBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0,0,0,0)
		self.widget.setLayout(self.layout)

		self.filters = self.initFilters()
		self.layout.addWidget(self.filters, 1)
		self.filters.setFocus(QtCore.Qt.FocusReason.ActiveWindowFocusReason)

		self.packageGrid = self.initPackageGrid()
		self.layout.addWidget(self.packageGrid, 2)

		self.show()

	def initToolbar(self):
		toolbar = self.addToolBar('')
		toolbar.setMovable(False)
		toolbar.setContentsMargins(8, 0, 8, 0)

		pkgmanager = Qt.QComboBox()
		toolbar.addWidget(pkgmanager)
		pkgmanager.insertItems(1, ["Homebrew", "Pip", "Apt"])

		exitAct = Qt.QAction(QIcon('./src/main/icons/base/64.png'), 'Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(Qt.qApp.quit)
		toolbar.addAction(exitAct)

		toolbar.addSeparator()

		spacer = Qt.QWidget()
		spacer.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
		toolbar.addWidget(spacer)

		searchbar = Qt.QLineEdit()
		toolbar.addWidget(searchbar)
		searchbar.setFixedWidth(120)

		return toolbar

	def initStatusbar(self):
		statusbar = self.statusBar()
		statusbar.showMessage('Ready')
		statusbar.setContentsMargins(8, 0, 8, 0)

		progress = Qt.QProgressBar()
		progress.setFixedWidth(120)
		progress.setValue(0)

		statusbar.addPermanentWidget(progress)

		return statusbar

	def initFilters(self):
		filters = Qt.QListWidget()
		filters.setFixedWidth(160)

		filter_types = [
			Qt.QListWidgetItem("All"),
			Qt.QListWidgetItem("Installed"),
			Qt.QListWidgetItem("Not Installed"),
			Qt.QListWidgetItem("To Update")
		]
		for f in filter_types:
			filters.addItem(f)

		filters.setCurrentItem(filter_types[0])

		return filters

	def initPackageGrid(self):
		packageGrid = Qt.QTableView()

		return packageGrid



window = MainWindow()
exit_code = appctxt.app.exec_()
sys.exit(exit_code)
