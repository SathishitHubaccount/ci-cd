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
    assert add(0,0)==0
    assert add(-5,-10)==-15
    assert add(1.5,2.5)==4.0
    assert add(-1,1)==0

def test_sub():
    assert sub(5,3)==2
    assert sub(10,5)==5
    assert sub(3,5)==2  
    assert sub(0,0)==0
    assert sub(-5,5)==10  
    assert sub(5,-5)==10  
    assert sub(-10,-5)==5  

def test_mul():
    assert mul(2,3)==6
    assert mul(5,4)==20
    assert mul(-2,3)==-6
    assert mul(-2,-3)==6
    assert mul(0,5)==0
    assert mul(5,0)==0
    assert mul(0,0)==0
    assert mul(1,100)==100
    assert mul(-1,100)==-100

def test_div():
    assert div(6,2)==3.0
    assert div(10,5)==2.0
    assert div(7,2)==3.5
    assert div(-6,2)==-3.0
    assert div(6,-2)==-3.0
    assert div(0,5)==0
    assert div(5,0)==None
    assert div(0,0)==None  
    assert div(1,3)==1/3

def test_fact():
    assert fact(0)==1
    assert fact(1)==1
    assert fact(2)==2
    assert fact(3)==6
    assert fact(4)==24
    assert fact(5)==120
    assert fact(-1)==1  

def test_pi():
    import math
    assert pi()==math.pi
    assert abs(pi() - 3.14159) < 0.001

def test_percentage():
    assert percentage(50,100)==50
    assert percentage(25,100)==25
    assert percentage(1,4)==25
    assert percentage(0,100)==0
    assert percentage(100,100)==100
    assert percentage(75,300)==25
    assert percentage(1,3)==33  
    assert percentage(200,100)==200

def test_power():
    assert power(2,3)==8
    assert power(5,2)==25
    assert power(3,4)==81
    assert power(5,0)==1
    assert power(0,5)==0
    assert power(1,100)==1
    assert power(-2,2)==4
    assert power(-2,3)==-8
    assert power(2,-2)==0.25

def test_squar_root():
    assert squar_root(4)==2.0
    assert squar_root(9)==3.0
    assert squar_root(16)==4.0
    assert squar_root(25)==5.0
    assert squar_root(0)==0.0
    assert squar_root(1)==1.0
    assert abs(squar_root(2) - 1.414) < 0.001
    assert squar_root(0.25)==0.5