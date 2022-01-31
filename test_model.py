import requests as r
import pandas as pd
import json 

#base url is like this, but it will be given to us later
#base_url = "http://127.0.0.1:5000/"
# change to ec2 url if you upload to ec2
base_url = "http://ec2-18-219-99-248.us-east-2.compute.amazonaws.com:6000/"


#setting dataframe into json structure, then load into correct json structure.
test = pd.read_csv('test.csv')
test = test.to_json(orient = 'records')
test = json.loads(test)

response = r.post(base_url + 'predict', json = test)
if response.status_code == 200:
    print("...")
    print('Request successful')
    print('...')
    print(response.status_code)
    print(response.json())
else: 
    print(response.status_code)
    print('request failed')
    