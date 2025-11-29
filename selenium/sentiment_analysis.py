from textblob import TextBlob
import os
import json


def sentimen_analysis(title):
    filepath = os.path.join("Comment_Analysis", title, "comments.txt")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

        for episode in data:
            comments = data[episode]
            print(comments)


if __name__ == "__main__":
    sentimen_analysis("marriage-of-convenience")