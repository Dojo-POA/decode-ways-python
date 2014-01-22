from main import *

class TestGenerationOfPosibilities:
  def test_single_element(self):
    assert decode(1) == 'a'

  def test_two_elements(self):
    assert decode(10) == 'j'
    assert decode(11) == ['aa', 'k']
    