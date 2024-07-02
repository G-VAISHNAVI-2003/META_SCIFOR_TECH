from Cal import Cal


def test_adds():
    c = Cal()
    assert c.adds(1, 3) == 4
    assert c.adds(9, 4) == 13
    assert c.adds('a', 'b') is None

def test_subs():
    c = Cal()
    assert c.subs(9, 4) == 5
    assert c.subs(1, 3) == -2
    assert c.subs('a', 'b') is None


def test_mul():
    c = Cal()
    assert c.mul(2, 4) == 8
    assert c.mul(3, 0) == 0
    assert c.mul(1,2) is None

def test_div():
    c = Cal()
    assert c.div(19, 8) == 19 / 8
    assert c.div(10, 5) == 2
    assert c.div(5, 0) is None

# Test for the power method
def test_power():
    c = Cal()
    assert c.power(2, 3) == 8.0
    assert c.power(3, 2) == 9.0
    assert c.power('a', 'b') is None

