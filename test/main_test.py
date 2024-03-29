from main import *
from nose.tools import assert_equals

class TestGenerationOfPossibilities:
  def test_chr_from_int_min(self):
    assert_equals(chr_from_int(0), '')

  def test_chr_from_int_max(self):
    assert_equals(chr_from_int(27), '')
    assert_equals(chr_from_int(80000), '')


  def test_single_digit(self):
    assert_equals(decode(1), ['a'])
    assert_equals(decode(2), ['b'])
    assert_equals(decode(3), ['c'])
    assert_equals(decode(4), ['d'])
    assert_equals(decode(5), ['e'])
    assert_equals(decode(6), ['f'])
    assert_equals(decode(7), ['g'])
    assert_equals(decode(8), ['h'])
    assert_equals(decode(9), ['i'])

  def test_two_digits(self):
    assert_equals(decode(10), ['j'])
    assert_equals(decode(11), ['aa', 'k'])

  def xtest_three_digits(self):
    assert_equals(decode(111), ['aaa', 'ak', 'ka'])

  def test_five_digits(self):
    assert_equals(decode(88888), ['hhhhh'])
