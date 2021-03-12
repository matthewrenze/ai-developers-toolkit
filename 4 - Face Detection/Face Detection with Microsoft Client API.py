# Face Detection with Microsoft Client API

# Import libraries
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face import FaceClient

# Set the endpoint url
endpoint_url = "https://[your-service-endpoint].cognitiveservices.azure.com/"

# Set the subscription key
subscription_key = "[your-subscription-key]"

# Create the credentials
credentials = CognitiveServicesCredentials(subscription_key)

# Create a face-detection client
client = FaceClient(
    endpoint = endpoint_url, 
    credentials = credentials)

# Set the file path to the image file
image_file_path = "C:/Demos/4 - Face Detection/Input.jpg"

# Open the image file for binary reading 
image_file = open(
    file = image_file_path, 
    mode = "rb")

# Detect a single face
results = client.face.detect_with_stream(image_file)

# Get first result
result = results[0]

# Get the bounding box
bounding_box = result.face_rectangle

# Print the coordinates of the bounding box
print("Left: " + str(bounding_box.left))
print("Top: " + str(bounding_box.top))
print("Width: " + str(bounding_box.width))
print("Height: " + str(bounding_box.height))