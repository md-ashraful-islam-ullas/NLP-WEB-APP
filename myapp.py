from flask import Flask, render_template, request, redirect
from db import DataBase
from myapi import ner, sentiment_analysis, language_detection

app = Flask(__name__)
dbo = DataBase()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=["post"])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.insert(name, email, password)
    if response:
        return render_template('login.html', message="Registration Successfull. Login to proceed.")
    else:
        return render_template('register.html', message="Email already exist.")

@app.route('/perform_login', methods=["post"])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    
    response = dbo.search(email, password)
    if response:
        return redirect('/profile')
    else:
        return render_template('login.html',message_w='Incorrect email/password')
    
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner_page():
    return render_template('ner.html')


@app.route('/perform_ner', methods=["post"])
def perform_ner():
    text = request.form.get('ner_text')
    search_text = request.form.get('search_for')

    response = ner(text,search_text)
    print(response)
    return "something"

@app.route('/sentiment')
def sentiment_page():
    return render_template('sentiment.html')

@app.route('/perform_sentiment', methods=["post"])
def perform_sentiment():
    text = request.form.get('sentiment_text')
    response = sentiment_analysis(text)

    print(response)
    return "something"

@app.route('/lengdect')
def lengdect_page():
    return render_template('lengdect.html')

@app.route('/perform_lengdect', methods=["post"])
def perform_lengdect():
    text = request.form.get('lengdect_text')
    response = language_detection(text)
    print(response)
    return "something"
    

if __name__ == "__main__":
    app.run(debug=True)