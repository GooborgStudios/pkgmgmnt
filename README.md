# Gooborg Studios' pkgmgmnt (working title)
A cross-platform package manager GUI written in PyQt5 for Homebrew, Apt, Pip, and NPM.

**pkgmgmnt is currently in the initial development stages and is not ready for real use.**

## What is pkgmgmnt?
pkgmgmnt is a graphical interface for various package managers across all operating systems, written in Python and Qt5 for cross-platform convenience.  Back up from the command line and let the GUI do its magic.

## Is this a brand new package manager?
No, pkgmgmnt is an extension on your existing package manager, designed to help you spend less time writing commands, and more time writing code.  pkgmgmnt works with Homebrew, Apt, Pip, and NPM.

## How do I run it?
First off, you'll need Python 3, PyQt5, and FBS.  Python 3 can be installed through your favorite package manager (`brew install python`, `sudo apt install python3`, etc.) or via [download from python.org](https://www.python.org/downloads/).  Once downloaded, you can run `python3 -m pip install pyqt5 fbs` in the terminal to download the latest PyQt5 and FBS versions.

You can then run the program by going to the root of this repository and running `fbs run` in the terminal.  To package and bundle an app, run `fbs freeze` and then `fbs installer`.  Make sure to `fbs clean` before each freeze.

## How can I help?
Contributions are always welcome!  Like most repositories, a good start is to look through the issues tab and see what's available.  Or, if you want to work on something that's never been filed as an issue, simply submit a pull request.

## What about assisting financially?
We're more than happy to accept donations to our [PayPal](https://paypal.me/VinylDarkscratch).  Doing so gives you extra perks like your name listed on the About page, priority support/feature requests, and possibly even custom artwork from our team.  (Investors, please [contact us](https://www.gooborg.com), we'd love to talk with you!)

_Inspired by [Synaptic Package Manager](https://www.nongnu.org/synaptic/), [Cakebrew](https://www.cakebrew.com/), and [npm-gui](https://www.npmjs.com/package/npm-gui)._ 
