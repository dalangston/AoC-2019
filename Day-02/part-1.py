# Intcode interpreter

import csv

def parseFile(inFile):
  progs = []
  
  with open(inFile, 'r') as f:
    reader = csv.reader(f)
    progs = list(reader)

  for prog in progs:
    for i in range(len(prog)):
      prog[i] = int(prog[i])


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
    return -1

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

    try:
      program[out] = opr(d1, d2)
    except:
      print(f"Dumpting Program State\n\n{program}\n]n")
      exit(-1)

    pos += 4


#Original Input
#flightProg = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]

#Modified Input
flightProg = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]

#print(f"In : {flightProg}")
runOpCode(flightProg)
print(f"Out: {flightProg}")
