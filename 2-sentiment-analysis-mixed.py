# Sentiment analysis with mixed sentiment detection

from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    # Check for mixed sentiment
    if " and " in text or " but " in text:
        sentiments = [TextBlob(phrase).sentiment.polarity for phrase in text.split(" and ") if phrase]
        if any(sent > 0 for sent in sentiments) and any(sent < 0 for sent in sentiments):
            return "Mixed"

    # Standard sentiment analysis
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Example usage
texts = ["I love this phone and the battery life is bad",
         "The movie was great, but the ending was terrible",
         "I'm not sure how I feel about this new policy",
         "I love travelling"]

for text in texts:
    sentiment = analyze_sentiment(text)
    print(f"The sentiment of '{text}' is: {sentiment}")
