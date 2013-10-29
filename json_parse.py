#!/usr/bin/python

from __future__ import print_function
import json

def parse(filename):
    def remove_comments(dct):
        dct.pop('_comment',None)
        return dct
    with open(filename) as f:
        return json.load(f,object_hook=remove_comments)
    raise IOError("Could not read file " + filename)
