SublimeLinter-radon
================================

[![Build Status](https://travis-ci.com/christopherpickering/SublimeLinter-radon.svg?branch=master)](https://travis-ci.com/christopherpickering/SublimeLinter-radon)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [radon](https://radon.readthedocs.io/en/latest/index.html) cyclomatic complexity. It will be used with files that have the “python” syntax.

Any python function/class/method with a complexity over 5 will have a warning showing the current complexity values.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `radon` is installed on your system.

In order for `radon` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
