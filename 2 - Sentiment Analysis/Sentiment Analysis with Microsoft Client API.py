# Sentiment Analysis with Microsoft Client API

# Import libraries
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Set the endpoint url
endpoint_url = "https://text-analytics-1577.cognitiveservices.azure.com/"

# Set the subscription key
subscription_key = "[your-azure-subscription-key]"

# Create the credentials
credential = AzureKeyCredential(subscription_key)

# Create a text analytics client
client = TextAnalyticsClient(
    endpoint = endpoint_url,
    credential = credential)

# Create three text documents
documents = [
    "Hello World",
    "I love you!",
    "I hate you!"
]

# Analyze the sentiment of the documents
results = client.analyze_sentiment(
    documents = documents)

# Print the results
for result in results:
    print(f"Document: {result.sentences[0].text}")
    print(f" - Sentiment: {result.sentiment}")
    print(f" - Positive: {result.confidence_scores.positive:.2f}")
    print(f" - Neutral: {result.confidence_scores.neutral:.2f}")
    print(f" - Negative: {result.confidence_scores.negative:.2f}")
    print("")

