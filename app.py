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
    print("came in")
    age = request.form.get('age')
    print("age")
    person_home_ownership = request.form.get('person_home_ownership')
    print(person_home_ownership)
    if person_home_ownership=='Rent':
        person_home_ownership=3
    elif person_home_ownership=='Own':
        person_home_ownership=2
    elif person_home_ownership=='mortgage':
        person_home_ownership=0
    else:
        person_home_ownership=1
    person_income = float(request.form.get('person_income'))
    print(person_income)
    person_emp_length = float(request.form.get('person_emp_length'))
    print("Emp len")
    print(person_emp_length)
    loan_intent = request.form.get('loan_intent')
    print(loan_intent)
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
    loan_grade = request.form.get('loan_grade')
    print(loan_grade)
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
    loan_amnt = float(request.form.get('loan_amnt'))
    print(loan_amnt)
    loan_int_rate = float(request.form.get('loan_int_rate'))
    print(loan_int_rate)
    loan_percent_income = float(request.form.get('loan-percent-income'))
    print(loan_percent_income)
    cb_person_default_on_file = request.form.get('cb_person_default_on_file')
    
    print(request.form.get('option-1'), request.form.get('option-2'))
    if cb_person_default_on_file == 'N':
        cb_person_default_on_file = 0
    elif cb_person_default_on_file == 'Y':
        cb_person_default_on_file = 1
    print(cb_person_default_on_file)
    cb_person_cred_hist_length = float(request.form.get('cb_preson_cred_hist_length'))
    print(cb_person_cred_hist_length)

    data = np.array([
        [age, person_home_ownership, person_income, person_emp_length, 
         loan_intent, loan_grade, loan_amnt, loan_int_rate, 
         loan_percent_income, cb_person_default_on_file, cb_person_cred_hist_length]
    ])
    print(data)

    output = "No output"

    prediction = model.predict(data)
    if(prediction==0):
        output= "Congrats! You are eligible for the loan!!"
    else:
        output="Sorry! You are ineligible for the loan!"
  
    print(output)
    return render_template('index.html', prediction_text=output)

if __name__ == '__main__':
    app.run(debug=True, port=8001)

