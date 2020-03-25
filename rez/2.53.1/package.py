# -*- coding: utf-8 -*-

name = 'rez'

version = '2.53.1'

requires = ['python-2.7+<4']

variants = [['platform-windows', 'arch-AMD64', 'os-windows-10.0.18362.SP0']]

def commands():
    env.PYTHONPATH.append('{this.root}')

timestamp = 1581628325

format_version = 2
