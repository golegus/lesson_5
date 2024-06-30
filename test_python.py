from math import pi, sqrt, pow,hypot
import pytest

@pytest.fixture 
def numbers():
    return [1,2,3,4,5,-6,-7,-8,-9]

@pytest.fixture
def words():
    return ['apple', 'banana', 'grpe', 'ornge']

def test_filter_numbers(numbers):
    filtered_numbers=list(filter(lambda x: x % 2 == 0, numbers))
    assert filtered_numbers==[2, 4,-6, -8]


def filter_strings(words):
    filtered_words=list(filter(lambda x: 'a' in x, words))
    assert filtered_words==['apple', 'banana']

def abs_numbers(numbers):
    abs_numbers=list(map(abs,numbers))
    assert abs_numbers==[1,2,3,4,5,6,7,8,9]

def len_words(words):
    len_words=list(map(len,words))
    assert len_words==[5,6,4,5]

def reverse(numbers):
    rev_list=list(map(lambda x: x[::-1], numbers))
    assert rev_list == [-9, -8, -7, -6, 5,4,3,2,1]

def split_and_list():
    numbers="1 2 5 7 8 12 454 21 89 40 50 61"
    list_numbers=list(map(int,numbers.split()))
    assert list_numbers == [1, 2, 5, 7, 8, 12, 454, 21, 89, 40, 50]

# def numbers_sorted(numbers):
#     sorted_numbers=sorted(numbers, reverse=True)
#     sorted_numbers=sorted(numbers)

#     assert sorted_numbers == numbers


assert pi==3.141592653589793
assert sqrt(4)==2
assert sqrt(4)!=3
assert pow(3,2)==9
assert pow(9,3)!=10
assert pow(9,3)!=10
assert hypot(12,9)==sqrt(12*12+9*9)


