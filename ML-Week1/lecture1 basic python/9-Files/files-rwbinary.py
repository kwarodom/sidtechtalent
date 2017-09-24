#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    #with binary file have to use buffer IO and only use binary type
    buffersize = 50000
    infile = open('olives.jpg','rb') #open a file with binary mode
    outfile = open('new.jpg', 'wb') #write a file in binary mode
    buffer = infile.read(buffersize) #this one is not iterable
    while len(buffer):
        outfile.write(buffer)
        print('.', end='')
        buffer=infile.read(buffersize)
    print()
    print('Done!')

if __name__ == "__main__": main()
