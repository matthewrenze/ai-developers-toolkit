# Face Detection with Amazon Client API

# Import libraries
import boto3
import json
import base64

# Set the file path to the image file
image_file_path = "C:/Demos/4 - Face Detection/Input.jpg"

# Open the image file for binary reading 
image_file = open(
    file = image_file_path, 
    mode = "rb")

# Read the image data
image_data = image_file.read()

# Create an AWS client
client = boto3.client(
    aws_access_key_id = "[your-aws-access-key-id]",
    aws_secret_access_key = "[your-aws-secret-access-key]",
    service_name = "rekognition", 
    region_name = "us-west-2")

# Detect faces
results = client.detect_faces(
    Image = { "Bytes": image_data },
    Attributes = ["DEFAULT"])

# Get result
result = results["FaceDetails"][0]["BoundingBox"]

# Print the bounding box coordinates
print("Left: " + str(result["Left"]))
print("Top: " + str(result["Top"]))
print("Width: " + str(result["Width"]))
print("Height: " + str(result["Height"]))
