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

csv_headers = ['article_number', 'article_link', 'article_name', 'title_subjectivity', 'title_polarity', 'content_subjectivity', 'content_polarity', 'overall_score']
csv_content = []

with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title = TextBlob(row['article_name']).sentiment
        content = TextBlob(row['article_content']).sentiment

        csv_content.append({
            "article_number": row['article_number'],
            'article_link': row['article_link'],
            'article_name': row['article_name'],
            "title_subjectivity": title.subjectivity,
            "title_polarity": title.polarity,
            "content_subjectivity": content.subjectivity,
            "content_polarity": content.polarity,
            "overall_score": "N/A"
        })
        
        # TODO include the weighed calculation of the subjectvity and polarity based on heading and contnet


    outputFile = file.replace(".csv", "") + "-analysis.csv"
    try:
        with open(outputFile, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
            writer.writeheader()
            for data in csv_content:
                writer.writerow(data)
            print("Successfully created csv file: " + outputFile)
    except IOError:
        print("I/O error")