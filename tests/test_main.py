from src.main import anagram,length,nothing

def test_length():
    assert length("sathish")==7
    assert length([1,2,3,4,5])==5
    assert length([])==0
    