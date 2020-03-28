import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(r'C:\Users\bishn\OneDrive\Pictures\Demo Images\demo-image.jpg'),'Amit.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
#print(response.label_annotations[0])
labels = response.label_annotations
for i,annotation in enumerate(response.label_annotations):
	#print("{0}:{1}".format(annotation['description'],annotation['score']))
	temp = response.label_annotations[i]
	#print(temp['description'])
	print(response.label_annotations[i])


#print('Labels:')
#print(labels)
#for label in labels:
#    print(label.description)

