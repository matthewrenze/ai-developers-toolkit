# Sentiment Analysis with Google REST API

# Import libraries
import requests
import json

# Set the endpoint URL
url = "https://language.googleapis.com/v1/documents:analyzeSentiment"

# Set the subscription key
subscription_key = "[your-subscription-key]"

# Set the query-string parameters
params = { "key" : subscription_key }

# Set the request headers
headers = { "Content-type": "application/json" }

# Set the request body
body = { 
    "document":
        {
            "type": "PLAIN_TEXT",
            "language": "en",
            "content": "Hello World. I love you! I hate you!"
        }
    }

# Post the request
response = requests.post(
    url = url,
    params = params,
    headers = headers,
    json = body)

# Get the JSON response
results = response.json()

# Print the results
for result in results["sentences"] :
    text = result["text"]["content"]
    score = result["sentiment"]["score"]
    print(text + " = " + str(score))



