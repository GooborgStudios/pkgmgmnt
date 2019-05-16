# -*- coding: utf-8 -*-

# pkgmgmnt: pkgtable.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

from PyQt5 import QtCore
from PyQt5 import QtWidgets as Qt

class PkgTable(QtCore.QAbstractTableModel):
	"""
	keep the method names
	they are an integral part of the model
	"""
	def __init__(self, mylist, header, *args):
		super().__init__()
		self.mylist = mylist
		self.header = header

	def updateModel(self):
		self.layoutAboutToBeChanged.emit()
		self.dataChanged.emit(self.createIndex(0, 0), self.createIndex(self.rowCount(0), self.columnCount(0)))
		self.layoutChanged.emit()

	def rowCount(self, parent):
		return len(self.mylist)

	def columnCount(self, parent):
		return len(self.mylist[0])

	def data(self, index, role):
		if not index.isValid():
			return None
		if (index.column() == 0):
			value = self.mylist[index.row()][index.column()].text()
		else:
			value = self.mylist[index.row()][index.column()]
		if role == QtCore.Qt.EditRole:
			return value
		elif role == QtCore.Qt.DisplayRole:
			return value
		elif role == QtCore.Qt.CheckStateRole:
			if index.column() == 0:
				# print(">>> data() row,col = %d, %d" % (index.row(), index.column()))
				if self.mylist[index.row()][index.column()].isChecked():
					return QtCore.Qt.Checked
				else:
					return QtCore.Qt.Unchecked

	def headerData(self, col, orientation, role):
		if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
			return self.header[col]
		return None

	def sort(self, col, order):
		"""sort table by given column number col"""
		# print(">>> sort() col = ", col)
		if col != 0:
			self.layoutAboutToBeChanged.emit()
			self.mylist = sorted(self.mylist, key=operator.itemgetter(col))
			if order == QtCore.Qt.DescendingOrder:
				self.mylist.reverse()
			self.layoutChanged.emit()

	def flags(self, index):
		if not index.isValid():
			return None
		# print(">>> flags() index.column() = ", index.column())
		if index.column() == 0:
			# return Qt::ItemIsEnabled | Qt::ItemIsSelectable | Qt::ItemIsUserCheckable
			return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable
		else:
			return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

	def setData(self, index, value, role):
		if not index.isValid():
			return False
		if role == QtCore.Qt.CheckStateRole and index.column() == 0:
			self.mylist[index.row()][index.column()].setChecked(value == QtCore.Qt.Checked)
		self.dataChanged.emit(index, index)
		return True
