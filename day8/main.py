#!/usr/bin/env python
from util import *
from collections import defaultdict

class Instruction:
  def __init__(self, cols):
    self.register = cols[0]
    self.op = cols[1]
    self.operand = int(cols[2])
    if cols[3] != 'if':
      raise Exception('expected if')
    self.pred_register = cols[4]
    self.predicate = cols[5]
    self.pred_operand = int(cols[6])

  def satisfies_predicate(self, value):
    if self.predicate == '>':
      return value > self.pred_operand
    elif self.predicate == '<':
      return value < self.pred_operand
    elif self.predicate == '==':
      return value == self.pred_operand
    elif self.predicate == '!=':
      return value != self.pred_operand
    elif self.predicate == '<=':
      return value <= self.pred_operand
    elif self.predicate == '>=':
      return value >= self.pred_operand
    else:
      raise Exception('unknown predicate: {}'.format(self.predicate))

  def apply_op(self, cur_value):
    if self.op == 'inc':
      return cur_value + self.operand
    elif self.op == 'dec':
      return cur_value - self.operand
    else:
      raise Exception('unknown op: {}'.format(self.op))

instrs = []
for row in readsplits('input.txt'):
  instrs.append(Instruction(row))

highest_any_register = None
registers = defaultdict(int)
for instr in instrs:
  if instr.satisfies_predicate(registers[instr.pred_register]):
    registers[instr.register] = instr.apply_op(registers[instr.register])
    if highest_any_register is None or registers[instr.register] > highest_any_register:
      highest_any_register = registers[instr.register]

print(highest_any_register)
#print(registers)
#print('---')
#print(max(registers.items(), key=lambda x: x[1]))


