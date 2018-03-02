import sys
sys.path.append(".")

from LightUp.Lights import construct, LightGrid

def size():
    filename = 'test1.txt'
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
    
print(size())