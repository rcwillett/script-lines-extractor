# -*- coding: utf-8 -*-
import re

scriptFileName = input('Enter the name of the script file to read')
extractedLinesFileName = input('Enter the name of the file to export the script lines')
selectedCharacterName = input('Enter the name of the character to pull lines for (case sensative)')

script = open(scriptFileName, "r")
lines = open("{}.txt".format(extractedLinesFileName), "w")

saveNextLine = False
joinNextLine = False
prevLine = ''
saveLines = []

for line in script:
    cleanedLine = re.sub('^\s*', '', line)
    cleanedLine = re.sub('\s*$', '', cleanedLine)
    if (joinNextLine):
        cleanedLine = prevLine + ' ' + cleanedLine

    if (saveNextLine and (not re.match('.*[.?!]\s?$', cleanedLine, re.MULTILINE))):
        joinNextLine = True
        prevLine = re.sub('\s?$', '', cleanedLine)
    else:
        joinNextLine = False
        prevLine = ''

    if (not joinNextLine and saveNextLine and re.match('^[a-zA-Z]', cleanedLine)):
        saveLines.append(cleanedLine)
        lines.write(cleanedLine + '\n');
    elif (not joinNextLine and re.match(selectedCharacterName, cleanedLine)):
        saveNextLine = True
    elif (not joinNextLine):
        saveNextLine = False
    
script.close()
lines.close();