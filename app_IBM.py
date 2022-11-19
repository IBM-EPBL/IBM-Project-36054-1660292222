from flask import render_template,Flask,request
import numpy as np
import pickle
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "pYsrmaRyzz3LufvFxHnD2hbld7dSoiqu4iIsV0Rbk8Ry"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
app= Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login.html')
def login():
    return render_template('login.html')
@app.route('/procedure.html')
def procedure():
    return render_template('procedure.html')
@app.route('/bank login.html')
def bank():
    return render_template('bank login.html')
@app.route('/About.html')
def about():
    return render_template('About.html')
@app.route('/terms.html')
def terms():
    return render_template('terms.html')
@app.route('/register.html')
def register():
    return render_template('register.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
@app.route('/home.html')
def home1():
    return render_template('home.html')
@app.route('/prediction.html')
def formpg():
    return render_template('prediction.html')
@app.route('/rating.html')
def rat():
    return render_template('rating.html')
@app.route('/prediction.html',methods = ['POST'])
def predict():
    if request.method=='POST':
        name=request.form['Name']
        gender=request.form['gender']
        married=request.form['married']
        dependents=request.form['dependents']
        education=request.form['education']
        employed=request.form['employed']
        credit=request.form['credit']
        proparea=request.form['proparea']
        ApplicantIncome=float(request.form['ApplicantIncome'])
        CoapplicantIncome=float(request.form['CoapplicantIncome'])
        LoanAmount=float(request.form['LoanAmount'])
        Loan_Amount_Term=float(request.form['Loan_Amount_Term'])
        
    if gender == 'Male':
        gender = 1
    else:
        gender = 0

    if married == 'Yes':
        married = 1
    else:
        married = 0

    if education == 'Graduate':
        education = 0
    else:
        education = 1

    if employed == 'Yes':
        employed = 1
    else:
        employed = 0

    if dependents == '3+':
        dependents = 3
    if credit == 'Yes':
        credit = 1
    else:
        credit = 0     
    if proparea == 'Urban':
        proparea = 2
    elif proparea == 'Rural':
        proparea = 0
    else:
        proparea = 1


    features = [[gender,married,dependents,education,employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,credit,proparea]]
    #con_features = [np.array(features)]
    con_features = [np.array(features)]
    
    
    
    payload_scoring = {"input_data": [{"fields": ['gender','married','depend','education','self_emp','applicant_income','co_income','loan_amount','loan_term','credit_history','property_area'], "values":features}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/a4da3004-fab4-4770-b978-b1fb81b0b561/predictions?version=2022-11-12', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
    print("response_scoring")
    prediction = response_scoring.json()
    predict = prediction['predictions'][0]['values'][0][0]

    #prediction = model.predict(scale_features)
    if predict == 1:
        return render_template('approve.html',prediction_text ='Congratulations! You are eligible for loan')
    else:
        return render_template('reject.html',prediction_text ='Sorry You are not eligible for loan')


if __name__ == "__main__":
    app.run(debug=True)