from itertools import combinations

offset = 96

def chr_from_int(n):
  if n == ():
    return ''

  x = int(''.join(list(n)))
  if x <= 0 or x >= 27:
    return ''
  
  return chr(x+offset) 

def all_combinations(seq):
  for x in xrange(len(seq)):
    yield combinations(seq, x)

def decode(something):
  digits = str(something)
  head = digits[0]
  if head == 1 or head == 2:
    head+decode(something[1:]), decode
  return result


