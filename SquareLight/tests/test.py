import sys
sys.path.append(".")

from LightUp.Lights import construct, LightGrid

def test_N():
    file = '/TestData/sample.txt'
    N = utils.parseFile(file)
    assert N == 1000

def test_count():
    file = '/TestData/sample2.txt'
    grid = LightGrid(10)
    
    assert count(grid, 10) == 0
