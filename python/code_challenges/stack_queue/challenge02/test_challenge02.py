# Write your test here
import pytest
from challenge02 import Paranthesese

def test_close_open_parantheses():
    ''' method to test the givien paranthesees is valid or not'''
    p1 = Paranthesese()
    p2 = Paranthesese()
    
    
    p5 = Paranthesese()
    print(p1.isValid("()"))
    print(p2.isValid("()[]{}"))
    print(p5.isValid("[{(())}]"))

    assert p1.isValid("()") == True
    assert p2.isValid("()[]{}") == True
    assert p5.isValid("[{(())}]") == True

def test_close_open_parantheses2():
    ''' method to test the givien paranthesees with a string inside it is valid or not'''
    p4 = Paranthesese()
    print(p4.isValid("[(hello)()]"))
    assert p4.isValid("[(hello)()]")== True

def test_close_open_parantheses2_false():
    ''' method to ensure the givien misfit paranthesees is not valid '''
    p3 = Paranthesese()
    print(p3.isValid("[({}]"))
    assert p3.isValid(("[({}]")) == False
