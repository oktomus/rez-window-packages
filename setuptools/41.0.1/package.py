# -*- coding: utf-8 -*-

name = 'setuptools'

version = '41.0.1'

variants = [['platform-windows', 'arch-AMD64', 'os-windows-10.0.18362.SP0', 'python-3.8']]

def commands():
    env.PYTHONPATH.append('{this.root}/python')

timestamp = 1581628326

format_version = 2
