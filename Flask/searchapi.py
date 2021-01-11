# Python program to get a set of  
# places according to your search  
# query using Google Places API 

# importing required modules 
import requests, json
from pprint import pprint
  
# enter your api key here 
api_key = 'AIzaSyAjVxeC6dpeYlBF99Ab9tFnxhxLhMZU9nQ'

# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
  

# The text string on which to search 
query = 'vancouver' 


# get method of requests module 
# return response object 
r = requests.get(url + 'query=' + query + '&key=' + api_key) 



# json method of response object convert 
#  json format data into python format data 
x = r.json() 
  


for elem in x['results']:
	pprint(elem)

print(x['results'])

# now x contains list of nested dictionaries 
# we know dictionary contain key value pair 
# store the value of result key in variable y 
# y = x['results'] 

# keep looping upto length of y 
# for i in range(len(y)): 

    # Print value corresponding to the 
    # 'name' key at the ith index of y 
    # print(y[i]['name']) 