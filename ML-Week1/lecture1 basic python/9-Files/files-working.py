#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC
import re
import os

def main():
    
    '''
    #for small file we can copy it line by line
    infile = open('lines.txt','r') #default option 'r'for read,'w'for write,'a'for append,'r+'read or write,'rt'text file mode,'rb'binary file mode 
    outfile = open('new.txt', 'w')
    
    for line in infile:
        #print(line, file=outfile, end='') #write to a next file name outfile
        print(line, end='') #write to a next file name outfile
    print()    
    '''
    '''
    #wifiDevices
    wifiDevices=list() #This is a list of wifi Devices
    infile = open('wifidevices.txt','r') 
    for line in infile:
        #print(line, end='') #write to a next file name outfile
        match = re.search('http://',line) #have results in match
        #step2: replace the matched pattern with another text
        if match:
            s=line.split() #create a list object
            for string in s:
                match = re.search('http://',string) #have results in match
                if match:
                    print(string) 
                    wifiDevices.append(string)
            #print(line.replace(match.group(),'###'), end='') #call replace the match object
    print(wifiDevices) 
    print()
    '''
    
    #zigbeeDevices
    zigbeeDevices=dict(Coordinator=2,Router=3,user=4)
    print(zigbeeDevices)
    print(os.getcwd())
    '''
    zigbeeDevices=list() #This is a list of zigbee Devices
    infile = open('zigbeedevices.txt','r') 
    for line in infile:
        match = re.search('Device',line) #have results in match
        #step2: replace the matched pattern with another text
        if match:
             s=line.split() #create a list object
             print(s)
#              for string in s:
#                  match = re.search('http://',string) #have results in match
#                  if match:
#                      print(string) 
#                      wifiDevices.append(string)
#     print(zigbeeDevices) 
    print()
    '''
    
    '''
    #for big file -> we don't need to do it line by line instead we just use a buffer mode
    #use buffer to deal with a big chunk of file
    buffersize = 50000 #give buffersize = 50000 bytes 
    inbigfile = open('bigfile.txt', 'r')
    outbigfile = open('newbigfile.txt', 'w')
    buffer = inbigfile.read(buffersize)
    while len(buffer):
        outbigfile.write(buffer)
        print('.', end ='')
        buffer=inbigfile.read(buffersize)
    print()
    print('Done!')    
    '''
    
    
if __name__ == "__main__": main()
