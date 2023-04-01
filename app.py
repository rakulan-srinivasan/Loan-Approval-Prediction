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

@app.route('/index2',methods=['GET','POST'])
def index2():
    return render_template('index2.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    print("came in")
    age = float(request.form['age'])
    print("age")
    person_home_ownership = float(request.form['person_home_ownership'])
    print(person_home_ownership)
    person_income = float(request.form['person_income'])
    print(person_income)
    person_emp_length = float(request.form['person_emp_length'])
    print("Emp len")
    print(person_emp_length)
    loan_intent = float(request.form['loan_intent'])
    print(loan_intent)
    loan_grade = float(request.form['loan_grade'])
    print(loan_grade)
    loan_amnt = float(request.form['loan_amnt'])
    print(loan_amnt)
    loan_int_rate = float(request.form['loan_int_rate'])
    print(loan_int_rate)
    loan_percent_income = float(request.form['loan_percent_income'])
    print("Loan percent")
    print(loan_percent_income)
    cb_person_default_on_file = float(request.form['cb_person_default_on_file'])
    print("cb_default")
    print(cb_person_default_on_file)
    cb_person_cred_hist_length = float(request.form['cb_preson_cred_hist_length'])
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
  

    return render_template('index.html', prediction_text=output)

if __name__ == '__main__':
    app.run(debug=True, port=8001)
