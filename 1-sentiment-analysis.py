# Sentiment analysis of social media posts

from textblob import TextBlob


# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Example usage
#text = "who are you?"
text=input("Weka sentensi: ")
sentiment = analyze_sentiment(text)
print(f"The sentiment of the text is: {sentiment}")
