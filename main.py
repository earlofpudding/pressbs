from textblob import TextBlob
import csv
import glob, os

print("Pick a file to use as input\n")

fileList = glob.glob('data/*.csv')

for i in range(len(fileList)):
    print(str(i+1) + ": " + fileList[i])

filePick = input("")
while (int(filePick) not in range(len(fileList) + 1)):
    filePick = input("")

file = fileList[int(filePick) - 1]
print("You picked: " + file)

csv_headers = ['article_number', 'title_subjectivity', 'title_polarity', 'content_subjectivity', 'content_polarity', 'overall_score']

with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

        print(row['article_name'])
        print("For article " + row['article_number'])
        print("---------------------------")
        print("Title: ")

        title = TextBlob(row['article_name']).sentiment
        print(title.polarity)
        print(title.subjectivity)

        content = TextBlob(row['article_content']).sentiment
        print(content.polarity)
        print(content.subjectivity)