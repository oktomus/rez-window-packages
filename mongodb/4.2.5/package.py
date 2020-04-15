# -*- coding: utf-8 -*-

name = 'mongodb'
# https://www.mongodb.com/dr/fastdl.mongodb.org/win32/mongodb-win32-x86_64-2012plus-4.2.5-signed.msi/download

version = '4.2.5'

tools = ['mongo']

variants = []

def commands():
    env.PATH.append('{this.root}/bin')

timestamp = 1581628326

format_version = 2
