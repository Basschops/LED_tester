import requests
from urllib.parse import urlparse
import urllib.request
import sys
sys.path.append('.')

from LightUp.Lights import LightGrid
import argparse


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()

    filename = args.input
        
    if (urlparse(filename).netloc):
            urllib.request.urlretrieve(filename,"tempdata.txt")
            filename = 'tempdata.txt'

    with open(filename) as f:
        N = int(f.readline().strip())
        if N>1E9:
            print('N too large')
            exit()
    print("N is ",N)

    lights = LightGrid(N)
    
    lights.parse_file(filename, lights, N)
    
    print("Number of lights on: ", lights.count(lights, N))






