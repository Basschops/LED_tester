# -*- coding: utf-8 -*-
import re


from itertools import count

import requests
from urllib.parse import urlparse
import urllib.request
import sys
sys.path.append('.')
import argparse

class LightGrid:
    
    lights = None
    
    def __init__(self, N):
        self.lights = [[False]*N for _ in range(N)]
        
    #Make this class indexable
    def __getitem__(self, tup):
        x, y = tup
        return self.lights[x][y]
    #Make it possible to change values of the class grid
    def __setitem__(self, tup, value):
        x, y = tup
        self.lights[x][y] = value
        
    def parse_file(self, file, lights, N):
        # This needs to be a variable!!!!
        pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")        
        #pattern = re.compile(".*(turn on|turn off|switch)\s*([0-9]|[0-9][0-9]|[0-9][0-9][0-9]|1000)\s*,\s*([0-9]|[0-9][0-9]|[0-9][0-9][0-9]|1000)\s*through\s*([0-9]|[0-9][0-9]|[0-9][0-9][0-9]|1000),\s*([0-9]|[0-9][0-9]|[0-9][0-9][0-9]|1000).*")

        
        #Read in data file
        with open(file, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            
            match = re.match(pattern, line)
            
            #If the instructions are valid proceed
            if match != None: 
                print(match.group(0)) 
                
                coords = []
                commands = []
                CMD = match.group(0).replace(',', ' ')
                #This makes the CMD easy to split
                
                for s in CMD.split():
                    #This code accounts for negative numbers starting with '-'
                    if (s[0].isdigit() or s[0] == '-') and (s[1:].isdigit() or len(s)==1):
                        coords.append(int(s))
                    else:
                        commands.append(s)
                        
                #assign coordinates
                x1 = coords[0]
                y1 = coords[1]
                x2 = coords[2]
                y2 = coords[3]
                
                #Ensure that only the relevant range is affected
                #Size of array and last index are 1 different
                if x1>=N : x1=N-1
                if y1>=N : y1=N-1
                if x2>=N : x2=N-1
                if y2>=N : y2=N-1
                if x1<0 : x1=0
                if y1<0 : y1=0 
                if x2<0 : x2=0
                if y2<0 : y2=0
                
                #Apply the valid command to the class    
                lights.apply(lights, commands, x1, y1, x2, y2)

    
    def apply(self,lights, commands, x1, y1, x2, y2):
        '''Function that processes each valid command for the light grid'''
        #as there can be 1 or 2 terms for the instructions, the following branches are needed
        if commands[0] == 'turn' :
            if commands[1] == 'on':
                for j in range(y1,y2):
                    for i in range(x1,x2):
                        lights[i,j]== True
                
            if commands[1] == 'off':
                for j in range(y1, y2):
                    for i in range(x1,x2):
                        lights[i,j]== False
        elif commands[0] == 'switch':
            for j in range(y1, y2):
                for i in range(x1,x2):
                    if lights[i,j]== True:
                        lights[i,j]=False
                    else:
                        lights[i,j] = True
                        
    
    #Class to count the number of lights that are on
    def count(self,lights, N):
        count = 0
        for i in range(N):
            for j in range(N):
                if lights[i,j]==True:
                    count +=1
        return count

def construct():
    #Take input from arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()

    filename = args.input
    
    #Check if input is a url
    if (urlparse(filename).netloc):
            #Create new local file with data from url
            urllib.request.urlretrieve(filename,"tempdata.txt")
            filename = 'tempdata.txt'

    with open(filename) as f:
        N = int(f.readline().strip())
        #Check that N is in range
        if N>1E9:
            print('N too large')
            exit()
    print("Array size, N is ",N)

    lights = LightGrid(N)
    
    lights.parse_file(filename, lights, N)
    
    print("Number of lights on: ", lights.count(lights, N))

if __name__ == '__main__':
    pass

