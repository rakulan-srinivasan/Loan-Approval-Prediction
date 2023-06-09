from ast import parse
from urllib import response
import numpy as np
from flask import Flask, render_template, request
import pickle
import requests
import json
from datetime import date, datetime

app = Flask(__name__)

model = pickle.load(open('xgb_pkl.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    pred_input = [0.0]*11

    pred_input[0] = float(request.form.get('age'))

    pred_input[1] = float(request.form.get('person_income'))

    person_home_ownership = request.form.get('person_home_ownership')
    if person_home_ownership == 'rent':
        person_home_ownership = 3
    elif person_home_ownership == 'own':
        person_home_ownership = 2
    elif person_home_ownership == 'mortgage':
        person_home_ownership = 0
    pred_input[2] = float(person_home_ownership)

    pred_input[3] = float(request.form.get('person_emp_length'))

    loan_intent = request.form.get('loan_intent')
    if loan_intent=='PERSONAL':
        loan_intent=4
    elif loan_intent=='EDUCATION':
        loan_intent=1
    elif loan_intent=='MEDICAL':
        loan_intent=3
    elif loan_intent=='VENTURE':
        loan_intent=2
    elif loan_intent=='HOMEIMPROVEMENT':
        loan_intent=5
    else:
        loan_intent=0
    pred_input[4] = float(loan_intent)

    loan_grade = request.form.get('loan_grade')
    if loan_grade == 'A':
        loan_grade = 0
    elif loan_grade == 'B':
        loan_grade = 1
    elif loan_grade == 'C':
        loan_grade = 2
    elif loan_grade == 'D':
        loan_grade = 3
    elif loan_grade == 'E':
        loan_grade = 4
    pred_input[5] = float(loan_grade)

    pred_input[6] = float(request.form.get('loan_amnt'))

    pred_input[7] = float(request.form.get('loan_int_rate'))

    pred_input[8] = float(request.form.get('loan_percent_income'))

    cb_person_default_on_file = request.form.get('cb_person_default_on_file')
    if cb_person_default_on_file == 'N':
        cb_person_default_on_file = 0
    elif cb_person_default_on_file == 'Y':
        cb_person_default_on_file = 1
    pred_input[9] = float(cb_person_default_on_file)

    pred_input[10] = float(request.form.get('cb_person_cred_hist_length'))

    data = np.array([pred_input])

    prediction = model.predict(data)

    if(prediction[0] == 1):
        output = "Congrats! You are eligible for the loan!!"
    else:
        output = "Sorry! You are ineligible for the loan!"
  
    print(output)
    return render_template('index.html', prediction_text=output)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
