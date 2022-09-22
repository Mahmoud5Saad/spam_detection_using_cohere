import cohere
from cohere.classify import Example

from secret import API_KEY

co = cohere.Client(API_KEY)
response = co.classify(
  model='cda275be-c104-4769-8180-504560d7e72c-ft',
  inputs=["you may now claim your FREE CAMERA PHONE upgrade. We value you as a customer and want to give you the best service. It will only cost delivery charges $50!"])
print('The confidence levels of the labels are: {}'.format(response.classifications))
f = open("response.txt", "a")
f.write('The confidence levels of the labels are: {}'.format(response.classifications))
f.close()