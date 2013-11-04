#!/usr/bin/pyton

import rewrite_file
from os.path import abspath, join as pjoin, isdir

def rewrite_dir(dirname,mappings=None,target_dir=None):
    dirname = abspath(dirname)
    if not target_dir:
        target_dir = pjoin('/tmp',dirname[1:])
    if not mappings:
        mappings = json_parse.parse('link_dictionary.json')
    file_queue = os.listdir(dirname)
    for f in file_queue:
        filename = pjoin(dirname,f)
        if isdir(filename):
            rewrite_dir(filename,mappings,pjoin(target_dir,f))
        else:
            rewrite_file.rewrite_and_save(filename,mappings,pjoin(target_dir,f))

if __name__ == '__main__':
    rewrite_dir(sys.argv[1])
