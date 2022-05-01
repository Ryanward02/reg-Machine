global regs
global curIns
curIns = 0
regs = []

class Program:
    def __init__(self, startConf, instrList):
        global regs
        global curIns
        
        curIns = startConf[0]
        
        regs = startConf[1:]
        self.instrList = instrList

    def execute(self):
        print(curIns, regs)
        while (isinstance(self.instrList[curIns], Halt) != True):
            
            self.instrList[curIns].execute()
            print(curIns, regs)

def insToString(label, instr):
    isMinus = isinstance(instr, Minus)
    isPlus = isinstance(instr, Plus)
    
    if isMinus:
        print("L" + str(label) + ": R" + str(instr.reg) + "- -> L" + str(instr.instr1) + ", L" + str(instr.instr2))

    elif isPlus:
        print("L" + str(label) + ": R" + str(instr.reg) + "+ -> L" + str(instr.instr))

    else:
        print("L" + str(label) + ": HALT")

def numToInstr(n: int):
    binRep = str(bin(n))[2:]
    x = 0
    for i in range(len(binRep), 0, -1):
        print(i)
        val = binRep[i - 1]
        if val == 0:
            x += 1
        else:
            binRep = binRep[:i - 1]
            break
            
        
    print("<<" + str(x) + ", " + str(int("0b" + binRep, base=2)) + ">>")

class Halt:
    global regs
    global curIns
        
    def execute():
        print(curIns, regs)

class Plus:
    global p
    def __init__(self, reg, instr):
        self.reg = reg
        self.instr = instr

    def execute(self):
        global regs
        global curIns
        
        regs[self.reg] += 1
        curIns = self.instr

class Minus:
    def __init__(self, reg, instr1, instr2):
        self.reg = reg
        self.instr1 = instr1
        self.instr2 = instr2

    def execute(self):
        global regs
        global curIns
        if regs[self.reg] == 0:
            
            curIns = self.instr2
        else:
            
            regs[self.reg] -= 1
            curIns = self.instr1

pExample = Program([0, 3, 0], [Minus(0, 1, 2), Plus(1, 0), Halt()])

p = Program([0, 0, 7], [Minus(1, 2, 1), Halt(), Minus(1, 3, 4), Minus(1, 5, 4), Halt(), Plus(0, 0)])

## Print out program (print each instruction)
for i in p.instrList:
    insToString(p.instrList.index(i), i)

p.execute()
