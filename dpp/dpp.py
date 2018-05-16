#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import argparse

__all__ = ["main"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile", help="The file to preprocess")
    parser.add_argument("--output", "-o", help="The file to write to")

    args = parser.parse_args()

    if args.inputfile is None or not os.path.isfile(args.inputfile):
        parser.print_usage()
        exit(1)

    with open(args.output, "w") as f:
        ret = preproc(args.inputfile)
        f.writelines(ret)

    print "Done"

included_files = []
def preproc(filename, from_file = "", from_line = 0):
    included_files.append(filename)

    apath, _ = os.path.split(filename)
    ret = ""
    with open(filename, "r") as f:
        r = f.readlines()
        for i, l in enumerate(r):
            if l.startswith("<--"):
                include = os.path.join(apath, l[3:].strip())
                afile = os.path.abspath(include)
                if afile in included_files:
                    raise UnboundLocalError("""Loop detected in inclusion of %s
                    in %s:%d""" % (filename, from_file, from_line))

                if not os.path.isfile(afile):
                    raise IOError("File to include %s not found" % afile)

                ret += preproc(afile, filename, i+1)
            else:
                ret += l

    included_files.remove(filename)
    return ret


if __name__ == '__main__':
    main()
