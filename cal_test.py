from cal import add,sub,multiply,divide,square,power

def test_add():
    assert add(8, 9) == 17
    assert add(-1, -1) == -2
def test_sub():
    assert sub(9, 8) == 1
    assert sub(2, -9) == 11
def test_mul():
    assert multiply(0, 9) == 0
def test_divide():
    assert divide(9, 0) == "Invalid"
    assert divide(8, 4) == 2
def test_power():
    assert power(9, 0) == 1
def test_square():
    assert square(5) == 25