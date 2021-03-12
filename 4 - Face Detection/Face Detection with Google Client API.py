# Face Detection with Google Client API

# Import libraries
import os
from google.cloud import vision

# Set an environment variable pointing to the credentials file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Demos/[your-google-app-credentials-file].json"

# Create a image-annotation client
client = vision.ImageAnnotatorClient()

# Set the file path to the image file
image_file_path = "C:/Demos/4 - Face Detection/Input.jpg"

# Open the image file for binary reading 
image_file = open(
    file = image_file_path, 
    mode = "rb")

# Read the image data
image_data = image_file.read()

# Create image
image = vision.Image(
    content = image_data)

# Detect faces
results = client.face_detection(
    image = image)

# Get the first result
result = results.face_annotations[0]

# Get the bounding box
bounding_box = result.fd_bounding_poly

# Print the vertices for the bounding box
for vertex in bounding_box.vertices:
    x = str(vertex.x)
    y = str(vertex.y)
    print("Vertex: (" + x + "," + y + ")" )