# Intcode interpreter

import csv

def runTest(prog):
  print(prog)
  runOpCode(prog)
  print(prog)

def printState(op, data1, data2, outPos):
  sep = "=" * 15

  print(f"\n{sep}")
  print(f"Operation: {op}\nData 1: {data1}\nData 2: {data2}\nOut Inx: {outPos}")
  print(f"{sep}\n")

def getOpr(opCode):
  ops = {
    1:lambda x,y:x+y,
    2:lambda x,y:x*y,
    }
  
  if opCode in ops:
    return ops[opCode]
  else:
    print("Illigal OpCode")
    exit(-1)

def runOpCode(program):
  pos = 0
  prog_len = len(program)

  while pos <= prog_len:
    opCode = program[pos]
    
    if opCode == 99:
      #print("End of Program Reached")
      break

    opr = getOpr(opCode)

    d1 =  program[program[pos + 1]]
    d2 =  program[program[pos + 2]]
    out = program[pos + 3]

    #printState(opr, d1, d2, out)    

    program[out] = opr(d1, d2)
    pos += 4


#test_prog = [1,0,0,0,99]

#runTest(test_prog)

inputs = 'test-input'

with open(inputs, 'r') as f:
  reader = csv.reader(f)
  progs = list(reader)

for prog in progs:
  for i in range(len(prog)):
    prog[i] = int(prog[i])

for prog in progs:
  print(f"In : {prog}")
  runOpCode(prog)
  print(f"Out: {prog}")
