from fastapi import FastAPI

from textblob import TextBlob

app = FastAPI()

def get_sentiment_score(text):
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity
    return sentiment_score

def generate_ratings(reviews):
    ratings = []
    for review in reviews:
        sentiment_score = get_sentiment_score(review)
        if sentiment_score > 0:
            ratings.append(5)
        elif sentiment_score < 0:
            ratings.append(1)
        else:
            ratings.append(3)
    return ratings

@app.post("/analyze_reviews/")
def analyze_reviews(reviews: list[str]):
    ratings = generate_ratings(reviews)
    result = [{"review": review, "rating": rating} for review, rating in zip(reviews, ratings)]
    return result

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)