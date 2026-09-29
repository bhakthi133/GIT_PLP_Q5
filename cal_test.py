from cal import add,sub

def test_add():
    assert add(8, 9) == 17
    assert add(-1, -1) == -2
def test_sub():
    assert sub(9, 8) == 1
    assert sub(2, -9) == 11