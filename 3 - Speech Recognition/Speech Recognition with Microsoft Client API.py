# Speech Recognition with Microsoft Client API

# Import libraries
import azure.cognitiveservices.speech as speech

# Set the subscription key
subscription_key = "[your-azure-subscription-key]"

# Set the service region
service_region = "eastus"

# Create a speech configuration
speech_config = speech.SpeechConfig(
    subscription = subscription_key,
    region = service_region)

# Set the audio file path
audio_file_path = "C:/Demos/3 - Speech Recognition/Input.wav"

# Create an audio configuration
audio_config = speech.audio.AudioConfig(
    filename = audio_file_path)

# Create a speech-recognition client
recognizer = speech.SpeechRecognizer(
    speech_config = speech_config,
    audio_config = audio_config)

# Get the result
result = recognizer.recognize_once()

# Print the recognized text
print(result.text)

