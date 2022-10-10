import pytest
from data_structures.hashtable import Hashtable

def test_exists():
    assert Hashtable

# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_get_nonexistent():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("banana")
    print('actual: ', actual)
    expected = None
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_unique_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set('banana', "used for sundaes")
    hashtable.set("strawberry", "taste good")
    actual = hashtable.keys()
    expected = {'apple', 'banana', 'strawberry'}
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_with_collisions():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("pplea", 'not used for apple sauce')
    hashtable.set('banana', "used for sundaes")
    actual = hashtable.keys()
    expected = {'apple', 'pplea', 'banana'}
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_in_range():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    index1 = hashtable.hash('apple')
    hashtable.set("pplea", 'not used for apple sauce')
    index2 = hashtable.hash('pplea')
    hashtable.set('banana', "used for sundaes")
    index3 = hashtable.hash('banana')
    assert 0 <= index1 <= hashtable.size
    assert 0 <= index2 <= hashtable.size
    assert 0 <= index3 <= hashtable.size

