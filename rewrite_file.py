#!/usr/bin/python

from __future__ import print_function

import sys, lxml.html
from os.path import join as pjoin

import json_parse

def rewrite_and_save(filename,mappings=None,new_filename=None):
    parsed_html = lxml.html.parse(filename)
    if not new_filename:
        new_filename = pjoin('/tmp/',filename)
    if not mappings:
        mappings = json_parse.parse('link_dictionary.json')
    print('STUB!')

if __name__ == '__main__':
    rewrite_and_save(sys.argv[1])
