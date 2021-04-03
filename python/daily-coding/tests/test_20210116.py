from days._20210116 import main


def test_main():
    assert main([5, 6, 1], 8) is False
    assert main([5, 6, 0], 6) is True
    assert main([1, 1, 1], 1) is False
    assert main([1, 1, 1], 2) is True
