# Sentiment Analysis with Google Cloud AI

# Import libraries
import os
from google.cloud import language_v1

# Set an environment variable pointing to the credentials file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Demos/[your-google-app-credentials-file].json"

# Create a language-service client
client = language_v1.LanguageServiceClient()

# Create the document
document = { 
    "type_": "PLAIN_TEXT",
    "language": "en",
    "content": "Hello World. I love you! I hate you!"
}

results = client.analyze_sentiment(
    document = document,
    encoding_type = language_v1.EncodingType.UTF8)

# Print the results
for result in results.sentences :
    print("Text: " + result.text.content)
    print("Score: " + str(result.sentiment.score))
    print("")
