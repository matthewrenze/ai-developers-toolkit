# Speech Recognition with Google Client API

# Import libraries
import os
from google.cloud import speech

# Set an environment variable pointing to the credentials file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Demos/[your-google-app-credentials-file].json"

# Create a speech client
client = speech.SpeechClient()

# Create a configuration
config = speech.RecognitionConfig(
    language_code = "en-US")

# Set the file path to the audio file
audio_file_path = "C:/Demos/3A - Speech Recognition/Input.wav"

# Open the audio file for binary reading 
audio_file = open(
    file = audio_file_path, 
    mode = "rb")

# Read the audio data
audio_data = audio_file.read()

# Create an audio configuration
audio = speech.RecognitionAudio(
    content = audio_data)

# Recognize speech
results = client.recognize(
    config = config,
    audio = audio)

# Get first speech-recognition result
result = results.results[0].alternatives[0]

# Print transcription
print("Text: " + result.transcript)

# Print the confidence score
print("Score: " + str(result.confidence))
