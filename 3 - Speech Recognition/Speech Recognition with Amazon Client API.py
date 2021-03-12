# Speech Recognition with Amazon Client API

# Import libraries
import boto3
import requests
import json

# Create an AWS client
client = boto3.client(
    aws_access_key_id = "[your-aws-acces-key-id]",
    aws_secret_access_key = "[your-aws-secret-access-key]",
    service_name = "transcribe", 
    region_name = "us-west-2")

# Set the URL of the audio file
audio_url = "https://[path-to-your-aws-s3-bucket]/Input.wav"

# Start transcription
client.start_transcription_job(
    TranscriptionJobName = "testing",
    Media = {"MediaFileUri" : audio_url },
    MediaFormat = "wav",
    LanguageCode = "en-US")

# Get transcription job
job = client.get_transcription_job(
    TranscriptionJobName = "testing")

# Get the transcription URL
transcription_url = job["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]

# Get the transcription
response = requests.get(
    url = transcription_url)

# Get the results as JSON
results = response.json()

# Get the transcription result
result = results["results"]["transcripts"][0]["transcript"]

# Print the transcription
print("Transcription: " + result["transcript"])