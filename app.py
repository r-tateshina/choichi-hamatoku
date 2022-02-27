from flask import Flask, render_template
import pandas as pd
import numpy as np
import datetime

app = Flask(__name__)

hamatoku = pd.read_pickle('1yearago.pkl')


def wayback(source):
    today = datetime.datetime.utcnow() + datetime.timedelta(hours=9) - \
        datetime.timedelta(days=1) * 365
    index = source.index[(source["date"]-today).abs().argsort()][0].tolist()
    print(index)
    tweets = source.loc[index-1:index+1]['url']
    results = []
    for tweet in tweets:
        print(tweet)
        results.append(tweet)
    return results


@app.route("/")
def ayearago():
    tweets = wayback(hamatoku)
    return render_template("tweets.html", tweets=tweets)


if __name__ == "__main__":
    app.run(debug=False)
