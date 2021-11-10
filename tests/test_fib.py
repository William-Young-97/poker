import lib.fib as f

def test_fib():
    assert f.fib(0) == 0
    assert f.fib(1) == 1
    assert f.fib(10) == 55