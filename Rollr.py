import re
import sys

lineNumber = 0
with open(sys.argv[1],'r') as jsCodeFile:
    for line in jsCodeFile:
        lineNumber+=1
        if re.match("\s*$", line):
            continue
        if not re.match(".+[\{\};][\s]*$", line):
            print("%d. Statement should end with a semicolon." % lineNumber)
        if re.match(".*[ \t]$", line):
            print("%d. Statement should not have trailing whitespace." % lineNumber)
        if re.match("\s*\{\s*", line):
            print("%d. Open curly brace should not stand-alone." % lineNumber)
        if re.search("\{.*\}", line):
            print("%d. Closing curly brace should stand-alone." % lineNumber)
        if re.search("(?<!=)==(?!=)", line):
            print("%d. Should only use strict equality." % lineNumber)
        regex = re.search("(\".*\")", line)
        if regex is not None and not re.search("'", regex.string[regex.start():regex.end()]):
            print("%d. Should use single quotes." % lineNumber)
        if re.search(";.*;", line):
            print("%d. Use only one statement per line." % lineNumber)
        if len(line) > 80:
            print("%d. Lines should not be longer than 80 characters." % lineNumber)
    if not re.match(".*\n$", line):
        print("%d. File %s should end with a newline character." % (lineNumber, sys.argv[1]))
