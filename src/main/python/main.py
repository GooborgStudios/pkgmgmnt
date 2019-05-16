# -*- coding: utf-8 -*-

# pkgmgmnt: main.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

import sys

from fbs_runtime.application_context import ApplicationContext
from PyQt5 import QtCore
from PyQt5 import QtWidgets as Qt
from PyQt5.QtGui import QIcon

from mainwindow import MainWindow

appctxt = ApplicationContext()
window = MainWindow()
exit_code = appctxt.app.exec_()
sys.exit(exit_code)
