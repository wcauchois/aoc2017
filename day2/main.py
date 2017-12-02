from itertools import permutations

def checksum(rows):
  diffs = [max(r) - min(r) for r in rows]
  return sum(diffs)

def checksum2(rows):
  thesum = 0
  for r in rows:
    (a, b) = [(a, b) for (a, b) in list(permutations(r, 2)) if a / b == a // b][0]
    thesum += a / b
  return thesum

def parse(s):
  return [[int(a.strip()) for a in l.split('\t') if a.strip() != ''] for l in s.split('\n') if l.strip() != '']

#print(open('input.txt').read())
print(checksum2(parse(open('input.txt').read())))

