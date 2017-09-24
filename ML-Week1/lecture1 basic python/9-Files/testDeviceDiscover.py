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
    #Name list of available devices
    wifiThermostats = ["CT-30","3M-50","Ecobee","Nest"]
    wifiLights = ["Philips Hue"]
    zigbeeSmartPlugs = ["Digi_SmartPlug"]
    zigbeeSensors = ["Digi_SmartSensor"]
    zigbeeThermostats=["Z100"]
    #supportDevices = dict(Thermostat=[wifiThermostats,zigbeeThermostats],SmartPlug=[zigbeeSmartPlugs],Light=[wifiLights],Sensor=[zigbeeSensors])
    #Step1: Create a dictionary for the supported devices
    supportDevices2=dict(wifiThermostat=wifiThermostats,wifiLight=wifiLights,zigbeeSmartPlug=zigbeeSmartPlugs,zigbeeSensor=zigbeeSensors,zigbeeThermostat=zigbeeThermostats)    
    #Step2: Classify the type of the found device 
    str = "CT-30 V1.94".split()
    for queryvalue in str:
        for k,v in supportDevices2.items(): #look up for catagory of the queryvalue
            if queryvalue in supportDevices2[k]:
                print(k)
                flag=1
                break
            else:
                flag = 0
        if flag == 1: 
            break
    if flag == 0:
        print('Device model not found, Currently we dont support this device')
        
    
        
    ''' 
    #wifiDevices
    wifiDevices=list() #This is a list of wifi Devices
    infile = open('wifidevices.txt','r') 
    for line in infile:
        pattern1 = re.compile('http://',re.IGNORECASE) #define pattern to find
        pattern2 = re.compile('/sys/',re.IGNORECASE) #use the pre-compiled pattern more efficient
        if re.search(pattern1, line): #search for a pattern in specific line
            s=line.split() #create a list object by splitting line into separate strings
            for string in s: #after get an individual string search for string that match pattern1
                if re.search(pattern1, string):
                    #print(string) #for debug purpose only
                    if re.search(pattern2, string): #then search for string that match pattern 2 
                        string = pattern2.sub('/tstat/ ',string) #replace the found pattern by /tstat
                        wifiDevices.append(string)
    #print all available fwifi devices 
    print("DeviceDiscoverAgent found {} wifi (USNAP module) devices".format(len(wifiDevices)))
    for wifiDevice in wifiDevices:
        print("wifi Device {0} address: {1}".format(wifiDevices.index(wifiDevice)+1,wifiDevice))
    print()
    
    
    
    
    #zigbeeDevices
    zigbeeDevices=list() #This is a list of zigbee Devices
    infile = open('zigbeedevices.txt','r') 
    for line in infile:
        match = re.search('Device',line) #have results in match
        if match:
            #print(line) #use for debud purpose only
            match = re.search('End User|Router',line) #have results in match
            if match:
                s=line.split() #create a list object
                for string in s:
                    if len(string)==16:
                        zigbeeDevices.append(string.upper())
    #print(zigbeeDevices) 
    print("DeviceDiscoverAgent found {} Zigbee devices".format(len(zigbeeDevices)))
    i=1
    for zigbeeDevice in zigbeeDevices:
        print("Zigbee Device {0} address: {1}".format(i,zigbeeDevices[i-1]))
        i+=1
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
