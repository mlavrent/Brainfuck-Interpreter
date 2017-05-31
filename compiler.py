import re

class BFcompiler(object):

    def __init__(self):
        # Initialize tape and dataPointer
        self.dataPointer = 0
        self.tape = [0 for x in range(30000)]
        self.errors = []
        
        # Errors:
        #   -1: Invalid character
        #   -2: Pointer out of bounds

    def parseBF(sourceCode):
        # Remove comments
        sourceCode = re.sub(r'[^\[\]+-<>.,]*', "", sourceCode)

        

    def pointerMovement(command):
        # command - string, either < or >
        if command == '>':
            self.dataPointer += 1
        elif command == '<':
            self.dataPointer -= 1
        else:
            self.errors.append(-1)

        if self.dataPointer < 0 or self.dataPointer > len(self.tape):
            self.errors.append(-2)

    def showOutput():
        print(chr(self.tape[self.dataPointer]))
    


sourceCode = """
Hello this is BF
>>.++[-abc]<<
dooggo
> helloo"""

parseBF(sourceCode)
