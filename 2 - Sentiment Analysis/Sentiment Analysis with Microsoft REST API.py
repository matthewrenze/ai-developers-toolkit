# Sentiment Analysis with Microsoft REST API

# Import libraries
import requests
import json

# Set the endpoint URL
url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.1/sentiment"

# Set the subscription key
subscription_key = "[your-azure-subscription-key]"

# Set the request headers
headers = {
    "Content-type": "application/json",
    "Ocp-Apim-Subscription-Key": subscription_key}

# Set the request body to the text to be translated
body = { 
    "documents": 
    [ 
        {
            "id" : "1",
            "language": "en",              
            "text": "Hello World"
        },
        {
            "id" : "2",
            "language": "en",
            "text": "I love you! :)"
        },
        {
            "id" : "3",
            "language": "en",
            "text": "I hate you! :("
        }
    ]
}

# Post the request
response = requests.post(
    url = url,
    headers = headers,
    json = body)

# Get the JSON results from the response
results = response.json()

# Print the results
for result in results["documents"] :
    print(result)

