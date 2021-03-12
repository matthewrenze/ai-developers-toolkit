# Face Detection with Google REST API

# Import libraries
import requests
import json
import base64

# Set the endpoint URL
url = "https://vision.googleapis.com/v1/images:annotate"

# Set the subscription key
subscription_key = "[your-subscription-key]"

# Set the query-string parameters
params = { "key" : subscription_key }

# Set the request headers
headers = { "Content-type": "application/json" }

# Set the file path to the image file
image_file_path = "C:/Demos/4 - Face Detection/Input.jpg"

# Open the image file for binary reading 
image_file = open(
    file = image_file_path, 
    mode = "rb")

# Read the image data
image_data = image_file.read()

# Encode the image as a base 64 byte array
image_base64 = base64.b64encode(image_data)

# Encode the base-64 byte array as a utf-8 string
image_string = str(image_base64, "utf-8")

# Set the request body
body = {
    "requests": [
        {
            "image" : {
                "content": image_string
        },
            "features": [
                {
                    "type": "FACE_DETECTION"
                }
            ]
        }
    ]
}

# Post the request
response = requests.post(
    url = url,
    params = params,
    headers = headers,
    json = body)

# Get the results as JSON
results = response.json()

# Get first face-detection result
result = results["responses"][0]["faceAnnotations"][0]

# Get the face bounding box
bounding_box = result["fdBoundingPoly"]["vertices"]

# Format the JSON for display
formatted_bounding_box = json.dumps(
    obj = bounding_box, 
    indent = 4)

# Print the bounding box
print(formatted_bounding_box)

# Print the confidence score
print(result["detectionConfidence"])