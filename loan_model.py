#import the required plugins
# building an API that hosts a model. 
from flask import Flask, request, jsonify
from flask_restful import Api, Resource 
import pickle
import pandas as pd
#api turns your app into an API, and resource sends
#things in and out

#initializing the flask
app = Flask(__name__)

#Wrap the app to the restful_api function. 
api = Api(app) #wrapping the app in a restful API

# Step 1.5: load our model
model = pickle.load(open('model.pickle', 'rb'))

#Step 2: Define our API resources
class Predict(Resource):

    def post(self):
        json_data = request.get_json()

        #For one observation, transposing the data, so index is a column.
        #df = pd.DataFrame(json_data.values(), index = json_data.keys()).transpose


        #Recieving multiple observations
        df = pd.DataFrame(json_data)

#model will return the prediction. 
        result = model.predict(df)
        return result.tolist()

#Step 3: assigning our endpoints
api.add_resource(Predict, '/predict')

#Step 4: run our API
#if __name__ == '__main__':
    #app.run(debug=True)

#Step 4: EC2 version being sent
if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 6000
    #can specify any port. 