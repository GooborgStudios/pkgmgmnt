# -*- coding: utf-8 -*-

# pkgmgmnt: main.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

import sys

from fbs_runtime.application_context import ApplicationContext
from PyQt5 import QtCore
from PyQt5 import QtWidgets as Qt
from PyQt5.QtGui import QIcon

from pkgtable import PkgTable
import pkgmanagers

accepted_managers = ["Apt", "Homebrew", "Pip"]

class MainWindow(Qt.QMainWindow):
	def __init__(self):
		super().__init__()
		self.packagemanager = 'Homebrew'
		self.__initUI()

	def __initUI(self):
		self.setUnifiedTitleAndToolBarOnMac(True)
		self.setWindowTitle('Package Manager - Gooborg Studios')

		self.resize(1024, 768)

		self.actions = self.__initActions()

		self.toolbar = self.__initToolbar()
		self.statusBar = self.__initStatusBar()
		self.menubar = self.__initMenubar()

		self.widget = Qt.QWidget()
		self.setCentralWidget(self.widget)
		self.layout = Qt.QHBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.widget.setLayout(self.layout)

		self.filters = self.__initFilters()
		self.layout.addWidget(self.filters, 1)
		self.filters.setFocus(QtCore.Qt.FocusReason.ActiveWindowFocusReason)

		self.packageGrid = self.__initPackageGrid()
		self.layout.addWidget(self.packageGrid, 2)

		self.show()

	def __initActions(self):
		actions = {}

		exitAct = Qt.QAction('Exit', self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(Qt.qApp.quit)
		actions['exit'] = exitAct

		openAct = Qt.QAction(QIcon('./src/main/icons/base/64.png'), 'Open', self)
		openAct.setShortcut('Ctrl+O')
		openAct.triggered.connect(Qt.qApp.quit)
		actions['open'] = openAct

		return actions

	def __initToolbar(self):
		toolbar = self.addToolBar('')
		toolbar.setMovable(False)
		toolbar.setContentsMargins(8, 0, 8, 0)

		pkgmanager = Qt.QComboBox()
		toolbar.addWidget(pkgmanager)
		pkgmanager.insertItems(1, accepted_managers)

		pkgmanager.setCurrentIndex(accepted_managers.index(self.packagemanager))

		# toolbar.addAction(self.actions['exit'])

		# toolbar.addSeparator()

		spacer = Qt.QWidget()
		spacer.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Minimum)
		toolbar.addWidget(spacer)

		searchbar = Qt.QLineEdit()
		toolbar.addWidget(searchbar)
		searchbar.setFixedWidth(120)

		return toolbar

	def __initStatusBar(self):
		statusBar = self.statusBar()
		statusBar.showMessage('PRE-ALPHA DEVELOPMENT VERSION')
		statusBar.setContentsMargins(8, 0, 8, 0)

		progress = Qt.QProgressBar()
		progress.setFixedWidth(120)
		progress.setValue(0)

		statusBar.addPermanentWidget(progress)

		return statusBar

	def __initMenubar(self):
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(self.actions['exit'])
		fileMenu.addAction(self.actions['open'])

		return menubar

	def __initFilters(self):
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

	def __initPackageGrid(self):
		packageGrid = Qt.QTableView()

		header = ['', '', 'Name', 'Version', 'Latest']
		# a list of (fname, lname, age, weight) tuples
		dataList = [
			[Qt.QCheckBox(""), '', 'python', '3.7.3', '3.7.3'],
			[Qt.QCheckBox(""), '', 'ruby', '2.5.5', '2.6.3'],
			[Qt.QCheckBox(""), '', 'zsh', '', '5.7.1'],
		]

		model = PkgTable(dataList, header)

		packageGrid.setModel(model)
		packageGrid.setSortingEnabled(True)
		packageGrid.sortByColumn(2, QtCore.Qt.SortOrder.AscendingOrder)

		packageGrid.resizeColumnToContents(0)
		packageGrid.resizeColumnToContents(1)

		return packageGrid

appctxt = ApplicationContext()
appctxt.app.setAttribute(QtCore.Qt.ApplicationAttribute.AA_DontShowIconsInMenus)
window = MainWindow()
exit_code = appctxt.app.exec_()
sys.exit(exit_code)
