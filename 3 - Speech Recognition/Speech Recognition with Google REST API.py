# Speech Recognition with Google Client API

# Import libraries
import requests
import json
import base64

# Set the endpoint URL
url = "https://speech.googleapis.com/v1p1beta1/speech:recognize"

# Set the subscription key
subscription_key = "[your-subscription-key]"

# Set the query-string parameters
params = { "key" : subscription_key }

# Set the request headers
headers = { "Content-type": "application/json" }

# Set the file path to the audio file
audio_file_path = "C:/Demos/3A - Speech Recognition/Input.wav"

# Open the audio file for binary reading 
audio_file = open(
    file = audio_file_path, 
    mode = "rb")

# Read the audio data
audio_data = audio_file.read()

# Encode the audio as a base 64 byte array
audio_base64 = base64.b64encode(audio_data)

# Encode the base-64 audio as a utf-8 string
audio_string = str(audio_base64, "utf-8")

# Set the request body to the text to be translated
body = {
    "config" : {
        "languageCode": "en-US"
    },
    "audio": {
        "content": audio_string
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

# Get first speech-recognition result
result = results["results"][0]["alternatives"][0]

# Print transcription
print(result["transcript"])

# Print the confidence score
print(result["confidence"])