from flask import render_template,Flask,request
import numpy as np
import pickle 
# from sklearn.preprocessing import scale
app= Flask(__name__, template_folder='templates')

# model = pickle.load(open("Rfmodel.pkl",'rb'))



@app.route('/')
def home():
    return render_template('home.html')
# @app.route('/login.html')
# def login():

# @app.route('/bank login.html')
# def bank():
#     return render_template('bank login.html')
# @app.route('/About.html')
# def about():
#     return render_template('About.html')
# @app.route('/terms.html')
# def terms():
#     return render_template('terms.html')
# @app.route('/register.html')
# def register():
#     return render_template('register.html')
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
# @app.route('/home.html')
# def home1():
#     return render_template('home.html')
# @app.route('/prediction.html')
# def formpg():
#     return render_template('prediction.html')
# @app.route('/rating.html')
# def rat():
#     return render_template('rating.html')



if __name__ == "__main__":
    app.run(debug=True)