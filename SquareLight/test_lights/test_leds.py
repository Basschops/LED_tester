import sys
#sys.path.append(".")

from LightUp.Lights import construct, LightGrid

def test_size():
    filename = 'test1.txt'
    lights = LightGrid(15)
    
    lights.parse_file(filename, lights, 15)  
    assert lights.count(lights, 15) == 225

def test_count():
    grid = LightGrid(10)
    
    assert grid.count(grid, 10) == 0
    
def test_turn_on_off():
    filename1 = 'test2.txt'
    filename2 = 'test4.txt'
    lights = LightGrid(10)
    lights.parse_file(filename1, lights, 10)  
    assert lights.count(lights, 10) == 25
    lights.parse_file(filename2, lights, 10)
    assert lights.count(lights, 10) == 20

def test_switch():
    filename = 'test3.txt'
    lights = LightGrid(10)
    lights.parse_file(filename, lights, 10)  
    assert lights.count(lights, 10) == 21    
    
