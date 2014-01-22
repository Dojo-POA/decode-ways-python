offset = 96

def chr_from_int(n):
  return chr(n+offset) if n != 0 else ''

def decode(something):
  if something <= 10:
    return [chr_from_int(something)]
  else:
    result = ["".join([chr_from_int(int(i)) for i in str(something)])]

    if something < 27: 
      result.append(chr_from_int(something))

    return result