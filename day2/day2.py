#!/usr/bin/env python3

opcode_arr = []

def process_op_code(opcode_arr, start, end) :
    op, pos1, pos2, output_pos = opcode_arr[start:end]
    if op == 1:
        opcode_arr[output_pos] = opcode_arr[pos1] + opcode_arr[pos2]
    elif op == 2:
        opcode_arr[output_pos] = opcode_arr[pos1] * opcode_arr[pos2]
    elif op == 99:
        return opcode_arr
    return opcode_arr

with open('day2input.txt', 'r') as f:
    opcode_str = f.readline()
    opcode_arr = opcode_str.strip('\n').split(',')
    opcode_arr = [int(x) for x in opcode_arr]

print(opcode_arr)

ind = 0
def find_noun_and_verb(opcode_arr):
    og_opcode_arr = opcode_arr[:]
    for i in range(100):
        for j in range(100):
            opcode_arr[1] = i
            opcode_arr[2] = j
            # Run duration of opcode procedure
            ind = 0
            while (ind < len(opcode_arr)) and (ind + 4 < len(opcode_arr)):
                opcode_arr = process_op_code(opcode_arr, ind, ind+4)
                ind += 4
            if opcode_arr[0] == 19690720:
                return opcode_arr
            else:
                opcode_arr = og_opcode_arr[:]

print(find_noun_and_verb(opcode_arr))