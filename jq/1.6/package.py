# -*- coding: utf-8 -*-

name = 'jq'
# https://stedolan.github.io/jq/

version = '1.6'

tools = ['jq']

variants = [['platform-windows', 'arch-AMD64', 'os-windows-10.0.18362.SP0']]

def commands():
    env.PATH.append('{this.root}/bin')

timestamp = 1581628326

format_version = 2
