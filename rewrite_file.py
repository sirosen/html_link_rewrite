#!/usr/bin/python

from __future__ import print_function

import sys, lxml.html, os
from os.path import join as pjoin, dirname, exists, abspath

import json_parse

def etree_text_replace(node,mappings):
    if node.text:
        for old,new in mappings.iteritems():
            node.text = node.text.replace(old,new)
    for child in node:
        etree_text_replace(child,mappings)

def rewrite_and_save(filename,mappings=None,new_filename=None):
    parsed_html = None
    with open(filename) as f:
        parsed_html = lxml.html.parse(f)
    if not parsed_html:
        raise IOError("Could not read file " + filename)
    if not new_filename:
        new_filename = pjoin('/tmp',abspath(filename)[1:])
    if not mappings:
        mappings = json_parse.parse('link_dictionary.json')

    def link_repl(oldlink):
        try:
            return mappings[oldlink]
        except:
            return oldlink

    root = parsed_html.getroot()
    root.rewrite_links(link_repl)
    etree_text_replace(root,mappings)

    # Race condition out the wazoo here, but it's not worth the effort
    # of making this more robust
    directory = dirname(new_filename)
    if not exists(directory):
        os.makedirs(directory)

    with open(new_filename,'w+') as f:
        print(lxml.html.tostring(parsed_html),file=f)

if __name__ == '__main__':
    rewrite_and_save(sys.argv[1])
