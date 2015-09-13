__author__ = 'Guard'
import re
import sys

jsCodeFile = open(sys.argv[1] ,'r')
lineNumber = 0

def check_semicolon(line):
    if(re.search(r'}', line) or re.search(r'{', line) or re.search(r';', line)):
        return
    elif(not line.strip()):
        return
    else:
        print((str(lineNumber) + '. Statement should end with a semicolon.'))

for line in jsCodeFile:
    lineNumber+=1
    check_semicolon(line)
