from src.main import anagram,length,nothing


def test_anagram():
    assert anagram("ab","ba")==True
    assert anagram("abc","bca")==True
    assert anagram("asb","bsssa")==True
    assert anagram("jhdihdihiod","jiidsdoao")==False
    assert anagram("Hi","")==False

def test_nothing():
    assert nothing()==None

    