#!/usr/bin/env python

from util import *
import sys

def step(banks):
  new_banks = banks[:]
  (idx, max_blocks) = max(enumerate(new_banks), key=lambda x: (x[1], -x[0]))
  new_banks[idx] = 0
  counter = max_blocks
  cur_idx = (idx + 1) % len(new_banks)
  while counter > 0:
    new_banks[cur_idx] += 1
    counter -= 1
    cur_idx = (cur_idx + 1) % len(new_banks)
  return new_banks

#banks = [0, 2, 7, 0]
banks = readsplits('input.txt', int)[0]
cur_banks = banks
seen_states = [(banks, 0)]
i = 0
while True:
  cur_banks = step(cur_banks)
  i += 1
  seen_items = [(b, i) for (b, i) in seen_states if b == cur_banks]
  if len(seen_items) > 0:
    #print(i) # answer to part 1
    print(i - seen_items[0][1]) # answer to part 2
    break
  seen_states.append((cur_banks, i))

