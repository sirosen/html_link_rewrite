#!/usr/bin/python

from __future__ import print_function
import json

def parse(filename):
    def remove_comments(dct):
        dct.pop('_comment',None)
        return dct
    return json.load(filename,object_hook=remove_comments)
