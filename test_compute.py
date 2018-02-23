from compute import divide
from compute import multiply

def test_divide():
    x = divide(1,2)
    print(x)
    assert x == 0.5

def test_multiply():
    assert multiply(2,2) == 4
