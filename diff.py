#!/bin/env python3

import difflib,sys

try:
    File1=sys.argv[1]
    File2=sys.argv[2]
except Exception as e:
    print('Error : %s'%e)
    print('Usage: diff.py file1 file2')

def readfile(filename):
    try:
        with open(filename) as f:
            File_Content=f.read().splitlines()
        return File_Content
    except Exception as e:
        print('Error: %s'%e)
def main():
    d=difflib.HtmlDiff()
    File1_Content=readfile(File1)
    File2_Content=readfile(File2)
    with open('/tmp/diff.html','w') as f:
        print(d.make_file(File1_Content,File2_Content),file=f)

if __name__ == '__main__':
    main()