
def thing(s):
  cur = None
  summ = 0
  for i in range(0, len(s)):
    cur = s[i]
    nex = s[(i + 1) % len(s)]
    if cur == nex:
      summ += int(cur)
  return summ


