# -*- coding: utf-8 -*-

name = 'rezgui'

version = '2.53.1'

tools = ['rez-gui']

requires = [
    'rez-2.53+<3',
    'PyQt-4'
]

variants = [['platform-windows', 'arch-AMD64', 'os-windows-10.0.18362.SP0']]

def commands():
    env.PYTHONPATH.append('{this.root}')
    env.PATH.append('{this.root}/bin')

timestamp = 1581628326

format_version = 2
