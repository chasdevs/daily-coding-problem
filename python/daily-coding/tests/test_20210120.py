from days._20210120 import cons, car, cdr

def test_main():
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4