# Face Detection with Microsoft REST API

# Import dependencies
import os
import json
import requests

# Set the endpoint URL 
url = "https://eastus.api.cognitive.microsoft.com/face/v1.0/detect"

# Set the subscription key
subscription_key = "[your-subscription-key]"

# Set the headers
headers = { 
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/octet-stream" }

# Set the file path to the image file
image_file_path = "C:/Demos/4 - Face Detection/Input.jpg"

# Open the image file for binary reading 
image_file = open(
    file = image_file_path, 
    mode = "rb")

# Read the image data
image_data = image_file.read()

# Post the request to the API
response = requests.post(
    url = url, 
    headers = headers, 
    data = image_data)

# Format the JSON response
formatted_json = json.dumps(
    obj = response.json(), 
    indent = 4)

# Print the formatted json
print(formatted_json)