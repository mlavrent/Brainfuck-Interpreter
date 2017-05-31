import re

class BFCompiler(object):

    def __init__(self):
        # Initialize tape and dataPointer
        self.dataPointer = 0
        self.instPointer = 0
        self.tape = [0 for x in range(20)]
        self.errors = []
        
        # Errors:
        #   -1: Invalid program character
        #   -2: Pointer out of bounds
        #   -3: Invalid input character
        #   -4: Invalid value

    def parseBF(self, sourceCode):
        # Remove comments
        sourceCode = re.sub(r'[^\[\]+-<>.,]*', "", sourceCode)
        self.sourceCode = sourceCode
        
        while self.instPointer < len(sourceCode):
            char = self.sourceCode[self.instPointer]
            if char == '>' or char == '<':
                self.pointerMovement(char)
                self.instPointer += 1
            elif char == '+' or char == '-':
                self.changeValue(char)
                self.instPointer += 1
            elif char == '.':
                self.showOutput()
                self.instPointer += 1
            elif char == ',':
                self.takeInput()
                self.instPointer += 1
            elif char == '[':
                self.instPointer += 1
                self.execLoop()
            else:
                self.errors.append(-1)

    def execLoop(self):
        while self.sourceCode[self.instPointer] != ']':
            char = self.sourceCode[self.instPointer]
            if char == '>' or char == '<':
                self.pointerMovement(char)
                self.instPointer += 1
            elif char == '+' or char == '-':
                self.changeValue(char)
                self.instPointer += 1
            elif char == '.':
                self.showOutput()
                self.instPointer += 1
            elif char == ',':
                self.takeInput()
                self.instPointer += 1
            elif char == '[':
                self.instPointer += 1
                self.execLoop()
            else:
                self.errors.append(-1)
        self.instPointer += 1

    def pointerMovement(self, command):
        # command - string, either < or >
        if command == '>':
            self.dataPointer += 1
        elif command == '<':
            self.dataPointer -= 1

        if self.dataPointer < 0 or self.dataPointer > len(self.tape):
            self.errors.append(-2)

    def changeValue(self, command):
        # command - string, either + or -
        if command == '+':
            self.tape[self.dataPointer] += 1
        elif command == '-':
            self.tape[self.dataPointer] -= 1

        if self.tape[self.dataPointer] < 0:
            self.errors.append(-4)

    def showOutput(self):
        print(chr(self.tape[self.dataPointer]))

    def takeInput(self):
        inVal = input("Input: ")
        value = inVal[0]

        if ord(value) < 0:
            errors.append(-3)

        self.tape[self.dataPointer] = ord(value)
    


sourceCode = """+++++++++[>++++++++++<-]>."""

bfc = BFCompiler()
bfc.parseBF(sourceCode)
