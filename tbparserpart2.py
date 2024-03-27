# PART 2 solution - recursive descent top-down parser by hand
from lexicalanalysis import build_the_lexer
from statements import *

lexer = build_the_lexer()

# define all the non terminal parsing functions
def tokerror(tok, exp):
  print(f"Unexpected token found: {tok.type}, Expecting: {exp}")
  print("INVALID")
  exit(1)

def program(tok):
  print(len(statements))
  actual_statement(tok)
  tok = lexer.token()
  while tok is not None:
    actual_statement(tok)
    tok = lexer.token()
  print(len(statements))
  print("VALID")

def actual_statement(tok):
  if tok.type != "NUMBER":
    tokerror(tok, "NUMBER")
  linenum = tok.value
  tok = statement(lexer.token(), linenum)
  if tok is None:
    print("EOF wihthout a newline character at the end")
    print("INVALID")
    exit(1)
  elif tok.type != "NEWLINE":
    tokerror(tok, "NEWLINE")

#note for all of these diffrerent types of statements we are creating a global statement variable that can be referenced whenever we need it.
def statement(tok, linenum):
  # look for a statement
  if tok.type == "PRINT":
    stmt = PrintStatement(linenum)
    tok = myprint(tok)
  elif tok.type == "INPUT":
    tok = myinput(tok)
  elif tok.type == "LET":
    let(tok)
    tok = lexer.token()
  elif tok.type == "GOTO":
    goto(tok)
    tok = lexer.token()
  elif tok.type == "GOSUB":
    gosub(tok)
    tok = lexer.token()
  elif tok.type == "IF":
    tok = myif(tok)
  elif tok.type == "END":
    tok = lexer.token()
  elif tok.type == "RETURN":
    tok = lexer.token()
  elif tok.type == "RND" or tok.type == "USR":
    function(tok)
    tok = lexer.token()
  elif tok.type == "REM":
    tok = lexer.token()
  else:
    tokerror(tok, "PRINT, INPUT, RETURN, END, ...")
  statements.append(stmt)
  return tok

def function(tok):
  tok = lexer.token()
  # insert your code here

def myif(tok):
  tok = lexer.token()
  tok = expression(tok)
  tok = relop(tok)
  tok = expression(tok)
  if tok.type != "THEN":
    tokerror(tok, "THEN")
  tok = lexer.token()
  tok = statement(tok)
  return tok
  # insert your code here

def relop(tok):
  if tok.type == "LESS":
    tok = lexer.token()
    if tok.type == "GREATER" or tok.type == "EQUALS":
      tok = lexer.token() #grab extra token since the token we checked was part of relop
  elif tok.type == "GREATER":
    if tok.type == "LESS" or tok.type == "EQUALS":
      tok = lexer.token()
  elif tok.type  == "EQUALS":
    tok = lexer.token()
  else: 
    tokerror(tok, "LESS, GREATER, EQUALS")
  return tok

def gosub(tok):
  tok = lexer.token()
  return tok
  # insert your code here

def goto(tok):
  tok = lexer.token()
  return tok
  # insert your code here

def let(tok):
  tok = lexer.token()
  return tok
  # insert your code here

def myinput(tok):
  tok = lexer.token()
  return tok
  # insert your code here

def myprint(tok):
  # no need to check for print token itself again, as that's the only way this function ends up being called
  tok = expr_list(lexer.token())
  return tok

def expr_list(tok):
  # look for an expression list
  if tok.type != "STRING":
    tok = expression(tok)
  else:
    tok = lexer.token()
  while tok is not None and (tok.type == "COMMA" or tok.type == "SEMICOLON"):
    tok = expression(lexer.token())
  return tok

# note that expression MUST make an extra call to lex before it finishes
# so we need to return that token to whoever called expression
def expression(tok):
  if tok.type == "PLUS" or tok.type == "MINUS":
    tok = lexer.token()
  tok = term(tok)
  while tok is not None and (tok.type == "PLUS" or tok.type == "MINUS"):
    tok = term(lexer.token())
  return tok

def term(tok):
  factor(tok)
  tok = lexer.token()
  while tok.type == "TIMES" or tok.type == "DIVIDE":
    factor(lexer.token())
    tok = lexer.token()
    if tok is None or tok.type == "NEWLINE":
      break
    else:
      print("uhoh")
  return tok

def factor(tok):
  if tok.type != "VAR" and tok.type != "NUMBER" and tok.type != "LPAREN":
    tokerror(tok, "VAR, NUMBER, LPAREN")
  if tok.type == "LPAREN":
    tok = lexer.token()
    tok = expression(tok)
    if tok.type != "RPAREN":
      tokerror(tok, "RPAREN")

# def main():
print("Program Start.")

# now, open a program and parse it
the_source_code1 = open("printsonly.tb", "r") #file 1
# the_source_code2 = open("hexdump.tb", "r") #file 2
# the_source_code3 = open("random.tb", "r") #file 3
# the_source_code4 = open("ifsonly.tb", "r")

print("Reading printsonly file...")
lexer.input(the_source_code1.read())
statements = []
program(lexer.token())
print("Printsonly file read!")

# print("Reading hexdump file...")
# lexer.input(the_source_code2.read())
# program(lexer.token())
# print("Hexdump file read!")

# print("Reading random file")
# lexer.input(the_source_code3.read())
# program(lexer.token())
# print("Random file read")

# print("Reading ifsonly file...")
# lexer.input(the_source_code4.read())
# program(lexer.token())
# print("ifsonly file read!")

print("Program End")

  #TODO: the rest of the blank functions

# if __name__ == "__main__":
#   main()
