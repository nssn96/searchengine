# Name : Surya Narayanan Nadhamuni Suresh
# UTA ID : 1001877873

from flask import Flask,render_template, request,url_for,flash
#import mysql.connector as mysql

# library to clean data
import re
# Natural Language Tool Kit
import nltk
# for Stemming purpose
from nltk.stem.porter import PorterStemmer

# to remove stopword
from nltk.corpus import stopwords
nltk.download('stopwords')



app = Flask(__name__)

#Reference used for NLP processing
#https://www.geeksforgeeks.org/python-nlp-analysis-of-restaurant-reviews/?ref=lbp
def searchWord(fields):
    #reading the text file the text file
    f = open("alice.txt",'r')
    lines = f.readlines()
    #print(lines)

    clean_txt=[]

    #Cleaning the data
    for i in lines:
        #converting all to lower cases
        txt = re.sub('[^a-zA-Z]', ' ', str(i))
        txt = txt.lower()

        #splitting to array
        txt = txt.split()

        #creating a stemmer object to take main stem of each word
        pStem = PorterStemmer()

        #stemming each word and removing stop words
        txt = [pStem.stem(word) for word in txt
                if not word in set(stopwords.words('english'))]
        
        #creating the string back from array elements
        txt = ' '.join(txt)

        clean_txt.append(txt)
    
    for i in clean_txt:
        print(i)






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',methods=['POST','GET'])
def recent():
    if request.method=='POST':
        dic={}
        for key,value in request.form.items():
            if value!='':
                dic[key]=value

        if dic:
            result=searchWord(dic)
            if result==[]:
                result=[]
                flash('No records of earthquake for above mentioned days')

        else:
            result=[]
            flash('Please enter values in the field')

        
    return render_template('index.html')








if __name__ == "__main__":
    app.run()