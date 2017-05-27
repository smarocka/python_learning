import fibonacci
import pytest

def test_mul():
    result=fibonacci.mul(4,3)
    assert result == 15

@pytest.mark.parametrize('a, b, expectedoutput',
                        [
                        (3,4,-1),
                        (4,2,2),
                        (3,3,0)
                        ])
def test_sub(a, b, expectedoutput):
    result=fibonacci.sub(a,b)
    assert result == expectedoutput
