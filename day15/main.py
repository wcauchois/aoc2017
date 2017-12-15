DIVISOR = 2147483647

class Generator:
  def __init__(self, factor, multiple, initial_value):
    self.factor = factor
    self.value = initial_value
    self.multiple = multiple

  def next(self):
    first = True
    while self.value % self.multiple != 0 or first:
      self.value = (self.value * self.factor) % DIVISOR
      first = False

  def rightmost_bits(self):
    return self.value & 0xffff

#gen_a = Generator(16807, 4, 65)
#gen_b = Generator(48271, 8, 8921)
gen_a = Generator(16807, 4, 722)
gen_b = Generator(48271, 8, 354)

if __name__ == '__main__':
  count = 0
  for i in range(0, 5000000):
    if gen_a.rightmost_bits() == gen_b.rightmost_bits():
      count += 1
    gen_a.next()
    gen_b.next()
  
  print(count)
