# -*- coding: utf-8 -*-

# pkgmgmnt: pkgmanagers/__init__.py
# Copyright (c) 2019, Gooborg Studios.  All rights reserved.

from .main import *

from .homebrew import Homebrew

managers = [Homebrew()]
