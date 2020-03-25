# -*- coding: utf-8 -*-

name = 'pip'

version = '19.1.1'

tools = ['pip']

variants = [['platform-windows', 'arch-AMD64', 'os-windows-10.0.18362.SP0', 'python-3.8']]

def commands():
    env.PYTHONPATH.append('{this.root}/python')
    env.PATH.append('{this.root}/bin')

timestamp = 1581628326

format_version = 2
