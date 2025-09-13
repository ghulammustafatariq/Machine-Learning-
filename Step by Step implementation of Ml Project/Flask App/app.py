import pandas as pd

## Flask App
from flask import Flask, request, render_template
import pickle
import numpy as np

model = pickle.load(open("E:\KRISH NAIK COURSE\Machine Learning\Step by Step implementation of Ml Project\Flask App\models/model.pkl", "rb"))
scaler = pickle.load(open("E:\KRISH NAIK COURSE\Machine Learning\Step by Step implementation of Ml Project\Flask App\models/scaler.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
## Index(['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'FWI', 'Classes', 'Region']
     
@app.route("/predict", methods=["POST","GET"])
def predict_data():
    if request.method == "POST":
        # Extract features from form
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        
        Classes = int(request.form.get("Classes"))
        Region = int(request.form.get("Region"))

        # Scale the features
        input_data = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])

        # Make prediction
        prediction = model.predict(input_data)
        print("Prediction is:", prediction)


        
    
        
        

    # Render the result
        return render_template("home.html", prediction_text=f"Predicted Value: {prediction[0]}")
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)

