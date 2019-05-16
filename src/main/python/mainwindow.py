# -*- coding: utf-8 -*-

# pkgmgmnt: mainwindow.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

from PyQt5 import QtCore
from PyQt5 import QtWidgets as Qt
from PyQt5.QtGui import QIcon

class MainWindow(Qt.QMainWindow):
	def __init__(self):
		super().__init__()
		self.__initUI()

	def __initUI(self):
		self.setUnifiedTitleAndToolBarOnMac(True)
		self.setWindowTitle('Package Manager - Gooborg Studios')

		self.resize(1024, 768)

		self.toolbar = self.__initToolbar()
		self.statusBar = self.__initStatusBar()

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

	def __initToolbar(self):
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

	def __initStatusBar(self):
		statusBar = self.statusBar()
		statusBar.showMessage('Ready')
		statusBar.setContentsMargins(8, 0, 8, 0)

		progress = Qt.QProgressBar()
		progress.setFixedWidth(120)
		progress.setValue(0)

		statusBar.addPermanentWidget(progress)

		return statusBar

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

		return packageGrid
