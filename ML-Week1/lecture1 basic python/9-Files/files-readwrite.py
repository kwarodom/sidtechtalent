]14#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    
    f = open('lines.txt','r') #default option 'r'for read,'w'for write,'a'for append,'r+'read or write,'rt'text file mode,'rb'binary file mode 
    
    for line in f.readlines():
        print(line, end = '')

if __name__ == "__main__": main()
