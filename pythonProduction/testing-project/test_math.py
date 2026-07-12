from main import is_even
from main import average



def test_is_even():
    assert(is_even(4)) == True

def test_average():
    assert(average([5,4,3,2,1])) == 3.0
    