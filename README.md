# pressbs
Sentiment analysis of press releases for public companies to develop hold/sell/buy reccomendations

## Steps
1. Develop csv file with required information (press release page, company name, time period)
2. Throw csv file into the main.py script

## Evaluation Method
Obtain polarity and sentiment for headline, and content and throw it into the below formula which applies a fixed factor rating for both properties




## Considerations and Variables

1. Industry
2. Marketcap/Size of Company
3. Diversification of Company (Products, Services, etc).
4. Geopolitical landscape (where company operates)

## Improvements

Develop polarity and sentiment for various paragraphs of article content and from there determine a method to evaluate which paragraph represents the article most thoroughly. (Will require modifying fetching script to not concatenate into a single string for `article_content`)

Train and develop a unique classification system for press releases as the sentiment analysis system for TextBlob utilizes (Naive Bayes Classifier) movie reviews as their training data set. This would require shifting to the base NLTK library and building off the their basic functions
