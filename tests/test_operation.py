from src.math_operation import add, sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(10,10)==20

def test_sub():
    assert(-1,-1)==0
    assert(5,2)==-3
