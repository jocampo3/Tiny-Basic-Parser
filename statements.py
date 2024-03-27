class Statement:
    def __init__(self, lineNumber):
        self.lineNumber = lineNumber
        self.tokens = []
    def addToken(self, token):
        self.tokens.append(token)

    def execute(self):
        print("ERROR: Statement.execute() never should have been called.")

class PrintStatement(Statement):
    def __init__(self, lineNumber):
        Statement.__init__(lineNumber)

    def execute(self):
        print("Called print execute.")