#!/usr/bin/python3
"""markdown2html module"""
from sys import argv, stderr, exit
from os.path import exists


if __name__ == '__main__':
    num_of_arg = len(argv[1:])
    if num_of_arg < 2:
        stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        exit(1)
    if not exists(f'{argv[1]}'):
        stderr.write(f'Missing {argv[1]}\n')
        exit(1)
    else:
        exit(0)
