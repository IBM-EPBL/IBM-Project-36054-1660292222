from flask import render_template,Flask,request
import numpy as np
import pickle 
# from sklearn.preprocessing import scale
app= Flask(__name__, template_folder='templates')

# model = pickle.load(open("Rfmodel.pkl",'rb'))



@app.route('/')
def home():
    return render_template('home.html')