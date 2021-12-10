#!/usr/bin/env python3

from parser import *
import sys


FILENAME = sys.argv[1]
LINT = True


if __name__ == '__main__':
    data = open(FILENAME).read()
    setup(LINT, FILENAME)
    do_parsing(data)
