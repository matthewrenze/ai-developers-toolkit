# Tabular Data Classification with AutoML

# Import libraries
import pandas as pd
import tensorflow as tf
import autokeras as ak
from sklearn.model_selection import train_test_split

# Set logging level to hide warnings
tf.get_logger().setLevel('ERROR')

# Set folder path
file_path = "C:/Demos/1 - Tabular Data Classification/Titanic.csv"

# Read the data into a data frame
data = pd.read_csv(file_path)

# Inspect the data set
data.head()
len(data)

# Split the data into training and test sets
train_x, test_x = train_test_split(
    data,
    test_size = 0.2)

# Inspect the size of the data sets
len(train_x)
len(test_x)

# Pop the last column off the data frame
train_y = train_x.pop("Survived")
test_y = test_x.pop("Survived")

# Inspect the training data set
train_x.head()
train_y.head()

# Inspect the test data set
test_x.head()
test_y.head()

# Create a structured data classifier
classifier = ak.StructuredDataClassifier(    
    max_trials = 5)

# Train the model
classifier.fit(
    x = train_x,
    y = train_y,
    epochs = 10)

# Summarize the best model
classifier.export_model().summary()

# Evaluate the model
score = classifier.evaluate(
    x = test_x,
    y = test_y)

# Inspect the accuracy
print(score[1])

# Will Rose survive the Titanic?
rose_x = pd.DataFrame(
    data = [{
        "Sex": "female",
        "Age" : 17,         
        "Family" : 2,
        "Class" : 1,
        "Fare" : 150.0,
        "Cabin" : "B",
        "Port" : "Southampton"}])

# Inspect Rose's data
rose_x.head()

# Predict if Rose will survive
classifier.predict(rose_x)[0][0]

# Will Jack survive?
jack_x = pd.DataFrame(
    data = [{
        "Sex": "male",
        "Age" : 20,         
        "Family" : 0,
        "Class" : 3,
        "Fare" : 15.0,        
        "Cabin" : "F",
        "Port" : "Southampton"}])

# Predict if Jack will survive
classifier.predict(jack_x)[0][0]
