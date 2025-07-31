from src.main import anagram, length , nothing , add ,sub,mul,div,fact,pi,percentage,power,squar_root 
import random

def test_anagram():
    assert anagram("ab","ba")==True
    assert anagram("abc","bca")==True
    assert anagram("asb","bsssa")==False
    assert anagram("jhdihdihiod","jiidsdoao")==False
    assert anagram("Hi","")==False

def test_nothing():
    assert nothing()==None

  

def test_add():
    assert add(0,1)==1
    assert add(20000,11111)==31111
    assert add(-100,100)==0

def test_sub():
    assert sub(0,1)==1
    assert sub(100,100)==0