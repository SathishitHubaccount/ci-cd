from src.main import add ,sub

def test_add():
    assert add(2,3)==5
    assert add(0,0)==0
    assert add(0,1000)==1000
    assert sub(10,100)==90
    assert sub(0,100)==100
    