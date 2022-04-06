# Name : Surya Narayanan Nadhamuni Suresh
# UTA ID : 1001877873

from flask import Flask,render_template, request,url_for,flash
#import mysql.connector as mysql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')







if __name__ == "__main__":
    app.run()