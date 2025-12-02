import os
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
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

    return mean_polarities

if __name__ == "__main__":
    print(sentiment_analysis_vader("marriage-of-convenience"))