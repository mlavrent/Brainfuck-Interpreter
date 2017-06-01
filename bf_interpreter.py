import re
import sys

class BFCompiler(object):

    def __init__(self):
        # Initialize tape and dataPointer
        self.dataPointer = 0
        self.instPointer = 0
        self.tape = [0 for x in range(20)]
        self.errors = []
        
        # Errors:
        #   0: Invalid program character
        #   1: Pointer out of bounds
        #   2: Invalid input character
        #   3: Invalid value
        #   4: Bracket not closed
        
        self.errorMessages = [
            "Invalid program character",
            "Pointer out of bounds",
            "Invalid input character",
            "Invalid value",
            "Bracket not closed"]

    def parseBF(self, sourceCode):
        # Remove comments
        sourceCode = re.sub(r'[^\[\]+-<>.,]*', "", sourceCode)
        self.sourceCode = sourceCode
        
        while self.instPointer < len(sourceCode):
            self.execNextCommand()

    def findMatchingBracket(self, openBracketPos):
        num = 0
        closeBracketPos = -1
        for i in range(openBracketPos, len(self.sourceCode)):
            char = self.sourceCode[i]
            if char == '[':
                num += 1
            elif char == ']':
                num -= 1
            if num == 0:
                closeBracketPos = i
                break
                
        if num != 0:  
            self.errors.append(4)
            
        return closeBracketPos

        
    def execLoop(self):
        loopStart = self.instPointer - 1
        loopEnd = self.findMatchingBracket(loopStart)

        while self.tape[self.dataPointer] != 0:
            while self.sourceCode[self.instPointer] != ']':
                self.execNextCommand()
                #print(self.instPointer)
                
            self.instPointer = loopStart + 1
            
        self.instPointer = loopEnd + 1
        
    def execNextCommand(self):
        #print(self.instPointer)
        #print(self.dataPointer)
        #print(self.tape)

        if self.errors:
            for error in self.errors:
                print(self.errorMessages[error])
            sys.exit()
        char = self.sourceCode[self.instPointer]
        self.instPointer += 1

        if char == '>' or char == '<':
            self.pointerMovement(char)
        elif char == '+' or char == '-':
            self.changeValue(char)
        elif char == '.':
            self.showOutput()
        elif char == ',':
            self.takeInput()
        elif char == '[':
            self.execLoop()
        else:
            self.errors.append(0)


    def pointerMovement(self, command):
        # command - string, either < or >
        if command == '>':
            self.dataPointer += 1
        elif command == '<':
            self.dataPointer -= 1

        if self.dataPointer < 0 or self.dataPointer > len(self.tape):
            self.errors.append(1)

    def changeValue(self, command):
        # command - string, either + or -
        if command == '+':
            self.tape[self.dataPointer] += 1
        elif command == '-':
            self.tape[self.dataPointer] -= 1

        if self.tape[self.dataPointer] < 0:
            self.errors.append(3)

    def showOutput(self):
        print(chr(self.tape[self.dataPointer]), end='')

    def takeInput(self):
        inVal = input("Input: ")
        value = inVal[0]

        if ord(value) < 0:
            errors.append(-3)

        self.tape[self.dataPointer] = ord(value)
    


sourceCode = """
++++++[>+++++++++++<-]>.< Print B
++++++[>++++++++<-]>.< Print r
++++[>----<-]>-. Print a
++++++++. Print i
+++++. Print n
--------. Print f
<+++[>+++++<-]>. Print u
<+++[>------<-]>. Print c
++++++++. Print k
"""

bfc = BFCompiler()
bfc.parseBF(sourceCode)
print("\nProgram complete")
