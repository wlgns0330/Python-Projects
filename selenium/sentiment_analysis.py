import os
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import emoji


def sentiment_analysis_vader(title):
    filepath = os.path.join("Comment_Analysis", title, "comments.txt")
    mean_polarities = []
    sent = SentimentIntensityAnalyzer()

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
        for episode in data:
            comments = data[episode]
            polarity = []

            for comment in comments:
                comment = emoji.demojize(comment)
                sentiment = sent.polarity_scores(comment)['compound']
                polarity.append(sentiment)

            mean_polarities.append(sum(polarity) / len(polarity))

    print("Vader sentiment analysis completed.")

    return mean_polarities

def sentiment_analysis_textblob(title):
    filepath = os.path.join("Comment_Analysis", title, "comments.txt")
    mean_polarities = []

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
        for episode in data:
            comments = data[episode]
            polarity = []

            for comment in comments:
                comment = emoji.demojize(comment)
                sent = TextBlob(comment).sentiment.polarity
                polarity.append(sent)

            mean_polarities.append(sum(polarity) / len(polarity))

    print("Textblob sentiment analysis completed.")

    return mean_polarities

def save_data(title):
    filepath = os.path.join("Comment_Analysis", title, "data.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        d = {}
        d["vader"] = sentiment_analysis_vader(title)
        d["textblob"] = sentiment_analysis_textblob(title)
        json.dump(d, f, ensure_ascii=False, indent=2)

    print("Data saved.")

if __name__ == "__main__":
    save_data("marriage-of-convenience")