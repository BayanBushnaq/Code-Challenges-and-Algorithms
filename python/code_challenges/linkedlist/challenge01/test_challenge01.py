# Write your test here
import pytest
from linkedlist.challenge01.challenge01 import Linkedlist

def test_linkedlist():
    actual = Linkedlist(5)
    expected = Linkedlist()
    assert actual == expected



