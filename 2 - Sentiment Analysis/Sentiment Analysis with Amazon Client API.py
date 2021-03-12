# Sentiment Analysis with Amazon Client API

# Import libraries
import boto3
import json

# Create an AWS client
client = boto3.client(
    aws_access_key_id = "[your-aws-access-key-id]",
    aws_secret_access_key = "[your-aws-secret-access]",
    service_name = "comprehend", 
    region_name = "us-west-2")

# Set the text to be analyzed
text = "I love you!"

# Detect sentiment
results = client.detect_sentiment(
    Text = text,
    LanguageCode = "en")

# Print detected sentiment
print("Sentiment: " + results["Sentiment"])

# Get confidence scores
scores = results["SentimentScore"]

# Print confidence scores
print("Positive Score: " + str(scores["Positive"]))
print("Negative Score: " + str(scores["Negative"]))
print("Neutral Score: " + str(scores["Neutral"]))
print("Mixed Score: " + str(scores["Mixed"]))



