# Speech Recognition with Microsoft REST API

# Import libraries
import requests
import json

# Set the endpoint URL
url = "https://eastus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1"

# Set the subscription key
subscription_key = "[your-azure-subscription-key]"

# Set the query-string parameters
params = { "language" : "en-US" }

# Set the request headers
headers = {
    'Content-type': 'audio/wav',
    'Ocp-Apim-Subscription-Key': subscription_key}

# Set the file path to the audio file
audio_file_path = "C:/Demos/3 - Speech Recognition/Input.wav"

# Open the audio file for binary reading
audio_file = open(
    file = audio_file_path, 
    mode = "rb")

# Read the audio data
audio_data = audio_file.read()

# Post the request
response = requests.post(
    url = url,
    params = params,
    headers = headers,
    data = audio_data)

# Get result as JSON
result = response.json()

# Print the recognized text
print(result["DisplayText"])