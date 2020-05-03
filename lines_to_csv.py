# -*- coding: utf-8 -*-
import re
import csv

linesFileName = input('Enter the name of the extracted lines file\n')
lineFile = open(linesFileName, 'r')

csvFileName = input('Enter the name of the csv to output\n')

linesArray = []

def filterEmpty(x):
    return x != ''


for line in lineFile:
    line = line.replace(',','')
    spacedLine = re.sub('([.!?\n])', r' \1', line)
    wordsArray = re.split('\s', spacedLine)
    wordsArray = list(filter(filterEmpty, wordsArray))
    linesArray.append(wordsArray)

csvFile = open('{}.csv'.format(csvFileName), 'w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['word1', 'word2'])
for line in linesArray:
    print(line)
    for index, word in enumerate(line):
        if (index == 0):
            csvWriter.writerow(['^', word])
        elif (index == (len(line) - 1)):
            csvWriter.writerow([word, '$'])
        else:
            csvWriter.writerow([word, line[index + 1]])

csvFile.close()