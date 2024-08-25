from django.shortcuts import render,redirect
from httpx import request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

DATA_FILE = r"C:\Users\KHAY_B\Desktop\New folder\HousePricePrediction\HousePricePrediction\saved_data.csv"

def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):
  
    data = pd.read_csv(r"C:\Users\KHAY_B\Desktop\New folder\HousePricePrediction\HousePricePrediction\ghana_house_data.csv")
    data = data.drop(['Address'], axis=1)
    X = data.drop("Price", axis=1)
    Y = data["Price"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.30)
    model = LinearRegression()
    model.fit(X_train, Y_train)

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])

    pred = model.predict(np.array([var1, var2, var3,  var4, var5]).reshape(1,-1))
    pred = round(pred[0])
    if pred < 0:
        pred = -pred

    price = "The predicted price is GHC " + str(pred) + ".00"

    
  # Save the data to CSV
    new_data = pd.DataFrame({
        'Income': [var1],
        'House_Age': [var2],
        'Number_of_Rooms': [var3],
        'Number_of_Bedrooms': [var4],
        'Average_Population': [var5],
        'Predicted_Price': [price]
    })

    # Check if file exists
    if os.path.exists(DATA_FILE):
        # Append to existing file
        new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        # Create new file
        new_data.to_csv(DATA_FILE, mode='w', header=True, index=False)

    # Render the result page
    return render(request, 'predict.html', {"result2": price})

def save_data(request):
    # Read the saved data
    if os.path.exists(DATA_FILE):
        saved_data = pd.read_csv(DATA_FILE)
    else:
        saved_data = pd.DataFrame()

    # Render the saved data
    return render(request, 'saved_data.html', {'saved_data': saved_data.to_dict(orient='records')})

def delete_row(request, row_index):
    if request.method == "POST":
        if os.path.exists(DATA_FILE):
            # Read the saved data
            saved_data = pd.read_csv(DATA_FILE)

            # Drop the row at the specified index
            if 0 <= row_index < len(saved_data):
                saved_data = saved_data.drop(index=row_index).reset_index(drop=True)

                # Save the updated data back to the file
                saved_data.to_csv(DATA_FILE, mode='w', header=True, index=False)

    # Redirect to the saved data page
    return redirect('save_data')


