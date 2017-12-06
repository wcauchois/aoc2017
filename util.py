def rmempty(coll):
  return list(filter(lambda x: x, coll))

def readlines(fname):
  with open(fname, 'r') as fh:
    return rmempty([l.strip() for l in fh.readlines()])

def readsplits(fname, transformer=None):
  t = transformer or (lambda x: x)
  return rmempty(
    [
      [t(c) for c in rmempty(l.split())]
      for l in readlines(fname)
    ]
  )

