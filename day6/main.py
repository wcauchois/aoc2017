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

banks = list(map(int, readsplits('input.txt')[0]))
cur_banks = banks
seen_states = [banks]
i = 0
while True:
  cur_banks = step(cur_banks)
  i += 1
  if cur_banks in seen_states:
    break
  seen_states.append(cur_banks)
print(i)

