import re
import sys

lineNumber = 0
with open(sys.argv[1],'r') as jsCodeFile:
    for line in jsCodeFile:
        lineNumber+=1
        if re.match("\s*$", line): continue
        if not re.match(".+[\{\};][\s]*$", line): print("%d. Statement should end with a semicolon." % lineNumber)
        if re.match(".*[ \t]$", line): print("%d. Statement should not have trailing whitespace." % lineNumber)
    if not re.match(".*\n$", line): print("%d. File %s should end with a newline character." % (lineNumber, sys.argv[1]))