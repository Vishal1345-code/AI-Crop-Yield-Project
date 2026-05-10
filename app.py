#for app

from flask import Flask, render_template, request
import pickle
import numpy as np
import random

app = Flask(__name__)

#  LOAD MODEL (THIS IS THE FIX)
model = pickle.load(open(r"C:\Users\KANZARIYA HARDIK\Desktop\AI_Crop_Project\model\model.pkl", 'rb'))

# Fake price function
def get_smart_price(crop, rainfall, temp):
    crop = crop.lower()

    base_prices = {
        "wheat": 2200,
        "rice": 1800,
        "maize": 1700,
        "bajra": 1500,
        "soybean": 4000,
        "sugarcane": 3000
    }

    base = base_prices.get(crop, 2000)

    # 🌧️ Rainfall effect
    if rainfall > 200:
        base -= 150   # more production → price down
    elif rainfall < 100:
        base += 150   # low production → price up

    # 🌡️ Temperature effect
    if temp > 30:
        base += 100   # heat stress → price up
    elif temp < 20:
        base -= 50

    # 📈 Market fluctuation
    final_price = base + random.randint(-100, 100)

    return final_price

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        state = int(request.form['State'])
        crop = int(request.form['Crop'])

        year = float(request.form['Year'])
        rainfall = float(request.form['Rainfall'])
        temp = float(request.form['Temperature'])
        area = float(request.form['Area'])

        features = [[state, crop, year, rainfall, temp, area]]

        prediction = model.predict(features)[0]

        crop_dict = {0: "wheat", 1: "rice", 2: "Sugarcane", 3: "Bajra", 4: "Maize", 5: "Soybean"}
        crop_name = crop_dict[crop]


        price = get_smart_price(crop_name, rainfall, temp)

        profit = prediction * price

        return render_template('index.html',
                               prediction=round(prediction, 2),
                               price=price,
                               profit=round(profit, 2))

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)