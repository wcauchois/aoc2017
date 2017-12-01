
def thing(s):
  cur = None
  summ = 0
  lenby2 = int(len(s) / 2)
  for i in range(0, len(s)):
    cur = s[i]
    nex = s[(i + lenby2) % len(s)]
    if cur == nex:
      summ += int(cur)
  return summ


