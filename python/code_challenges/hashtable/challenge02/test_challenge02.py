# Write your test here

import pytest
from challenge02 import firstRepeatedWord

def test_repeated_word():
    assert firstRepeatedWord("ASAC is a department at LTUC. ASAC teaches programming in LTUC.") == "ASAC"
    assert firstRepeatedWord("I am learning programming at ASAC.") == "No Repetition"

def test_repeated_word_is_empty():
    assert firstRepeatedWord("") == "No Repetition"

        
     






