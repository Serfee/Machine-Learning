# README
# Hello everyone, in here I (Kaenova | Bangkit Mentor ML-20) 
# will give you some headstart on createing ML API. 
# Please read every lines and comments carefully. 
# 
# I give you a headstart on text based input and image based input API. 
# To run this server, don't forget to install all the libraries in the
# requirements.txt simply by "pip install -r requirements.txt" 
# and then use "python main.py" to run it
# 
# For ML:
# Please prepare your model either in .h5 or saved model format.
# Put your model in the same folder as this main.py file.
# You will load your model down the line into this code. 
# There are 2 option I give you, either your model image based input 
# or text based input. You need to finish functions "def predict_text" or "def predict_image"
# 
# For CC:
# You can check the endpoint that ML being used, eiter it's /predict_text or 
# /predict_image. For /predict_text you need a JSON {"text": "your text"},
# and for /predict_image you need to send an multipart-form with a "uploaded_file" 
# field. you can see this api documentation when running this server and go into /docs
# I also prepared the Dockerfile so you can easily modify and create a container iamge
# The default port is 8080, but you can inject PORT environement variable.
# 
# If you want to have consultation with me
# just chat me through Discord (kaenova#2859) and arrange the consultation time
#
# Share your capstone application with me! 🥳
# Instagram @kaenovama
# Twitter @kaenovama
# LinkedIn /in/kaenova

## Start your code here! ##

import os
import uvicorn
import traceback
import tensorflow as tf
import numpy as np

from pydantic import BaseModel
from urllib.request import Request
from fastapi import FastAPI, Response, UploadFile
# Initialize Model
# If you already put yout model in the same folder as this main.py
# You can load .h5 model or any model below this line

# If you use h5 type uncomment line below
model = tf.keras.models.load_model('./nlp_model.h5')
# If you use saved model type uncomment line below
# model = tf.saved_model.load("./my_model_folder")

app = FastAPI()

# This endpoint is for a test (or health check) to this server
@app.get("/")
def index():
    return "Hello world from ML endpoint!"

# If your model need text input use this endpoint!
class RequestText(BaseModel):
    text:str
 
@app.post("/predict_review")
def predict_text(req: RequestText, response: Response):
    try:
        # In here you will get text sent by the user
        text = req.text
        print("Uploaded text:", text)
        
        # Predict the text
        result = model.predict(text)

        labels = ['Positive', 'Neutral', "Negative"] 
        label = labels[np.argmax(np.around(result))]
        
        return label
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return "Internal Server Error"

class RequestRating(BaseModel):
    predicted:str
    user_rating:list
@app.post("/new_ratings")
def predict_text(req: Request, response: Response):
    try:
        existing_ratings = req.user_rating
        predicted_sentiment = req.predicted

        total_rating = sum(existing_ratings)
        num_rating = len(existing_ratings)

        # Assign weights for different sentiment categories
        weights = {
            "Positive": 1.0,  # Increase the rating by 1.0
            "Neutral": 0.0,   # No change in the rating
            "Negative": -1.0  # Decrease the rating by 1.0
        }

        # Calculate the weight based on the sentiment and existing ratings
        weight = weights.get(predicted_sentiment, 0.0)

        if total_rating == 0:
            weight_factor = 1.0
            if num_rating == 0:
                weight_factor = 5.0
        else:
            weight_factor = abs(total_rating) / num_rating

        # Adjust the weight based on the weight factor
        weight_adjusted = weight * (1.0 - abs(weight_factor))

        # Update the overall rating
        total_rating += weight_adjusted

        # Limit the rating value between 0 and 5
        total_rating = max(0, min(5, total_rating))

        return {'total_rating': total_rating, 'new_ratings': existing_ratings.append(weight)}

    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return "Internal Server Error"



# Starting the server
# Your can check the API documentation easily using /docs after the server is running
port = os.environ.get("PORT", 8080)
print(f"Listening to http://0.0.0.0:{port}")
uvicorn.run(app, host='0.0.0.0',port=port)