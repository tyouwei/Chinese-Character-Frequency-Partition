import csv

# reading from graphics file, change all the dictionary.txt to filter dictionary.txt
readFile = "graphics.txt"
highFile = "high_frequency_graphics.txt"
mediumFile = "medium_frequency_graphics.txt"
lowFile = "low_frequency_graphics.txt"
csvFile = "hanziDB.csv"

# Reading a file
referenceFile = open(readFile,"r", encoding="utf-8")
file1 = open(highFile,"w", encoding="utf-8")
file2 = open(mediumFile,"w", encoding="utf-8")
file3 = open(lowFile,"w", encoding="utf-8")
db = open(csvFile,"r", encoding="utf-8")
csvreader = csv.reader(db)

dictionary = {}

for row in csvreader:
    char = str(row[1])
    freqRank = int(row[0])
    if char not in dictionary:
        dictionary[char] = freqRank

db.close()
data = referenceFile.readlines()

for line in data:
    #get character from graphics.txt or dictionary.txt
    currentChar = str(line[14])
    if currentChar in dictionary:
        print(currentChar)
        if dictionary[currentChar] <= 3300:
            file1.write(line)
        elif dictionary[currentChar] <= 6600:
            file2.write(line)
        else:
            file3.write(line)

referenceFile.close()
file1.close()
file2.close()
file3.close()