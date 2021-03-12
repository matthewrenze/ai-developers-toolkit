# Object Classification with Microsoft REST API
# (Object Detection + Image Classification)

# Import dependencies
import requests
import cv2

# Set the URL endpoint
url = "https://eastus.api.cognitive.microsoft.com/vision/v3.1/detect"

# Set the subscription key
subscription_key = "[your-subscription-key]"

# Set the headers
headers = { 
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/octet-stream" }

# Set the file path to the image file
image_file_path = "C:/Demos/6 - Object Classification/Input.jpg"

# Read the image from the file path
image = cv2.imread(image_file_path)

# Convert the image into a byte array
image_bytes = cv2.imencode(".jpg", image)[1].tobytes()

# Post the request to the API
detection_response = requests.post(
    url = url, 
    headers = headers, 
    data = image_bytes)

# Get the results
detection_results = detection_response.json()

# Get the second object from results
detection_result = detection_results["objects"][1]

# Get the bounding box
bounding_box = detection_result["rectangle"]

# Get the coordinates
x = bounding_box["x"]
y = bounding_box["y"]
w = bounding_box["w"]
h = bounding_box["h"]

# Crop the image
cropped_image = image[y:y+h, x:x+w]

# Show the cropped image
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey()

# Convert the image into a byte array
cropped_image_bytes = cv2.imencode(".jpg", cropped_image)[1].tobytes()

# Post the request to the API
classification_response = requests.post(
    url = url, 
    headers = headers, 
    data = cropped_image_bytes)

# Get classification results as JSON
classification_results = classification_response.json()

# Get first result
classification_result = classification_results["objects"][0]

# Print image class
print(classification_result["object"])

# Print confidence score
print(classification_result["confidence"])

# Print parent categories
print(classification_result["parent"]["object"])
print(classification_result["parent"]["parent"]["object"])
print(classification_result["parent"]["parent"]["parent"]["object"])
