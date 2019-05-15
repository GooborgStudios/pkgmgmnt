# -*- coding: utf-8 -*-

# pkgmgmnt: main.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

import sys

from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

appctxt = ApplicationContext()
window = QMainWindow()
window.resize(250, 150)
window.show()
exit_code = appctxt.app.exec_()
sys.exit(exit_code)
