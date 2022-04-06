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
from collections import Counter

import nltk.data
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize



app = Flask(__name__)
app.secret_key = 'random string'

#Reference used for NLP processing
#https://www.geeksforgeeks.org/python-nlp-analysis-of-restaurant-reviews/?ref=lbp
def searchWord(fields):

    #split string by single space
    chunks = re.split(' ', fields['word'])
    #print(chunks)
    if len(chunks)>1:
        new_string = chunks[1]+" "+chunks[0]
        #print(new_string)


    #reading the text file the text file
    f = open("text.txt",'r')
    lines = f.readlines()
    print(type(lines))

    s_lines={}
    #searching using the word and displaying the lines
    count=1
    for i,l in enumerate(lines):
        if (fields['word'] or new_string) in l:
            temp=[]
            #print("Instance "+str(count))
            for j in lines[i:i+3]:
                if j in ['\n', '\r\n']:continue
                else:temp.append(j)
            s_lines[count]=temp
            count=count+1

    clean_txt=[]
    
    #Cleaning the data
    for i in lines:
        #converting all to lower cases
        txt = re.sub('[^a-zA-Z]', ' ', str(i))
        txt = txt.lower()

        #splitting to array
        txt = txt.split()

        # #creating a stemmer object to take main stem of each word
        # pStem = PorterStemmer()

        #stemming each word and removing stop words
        txt = [word for word in txt
                if not word in set(stopwords.words('english'))]
        
        #creating the string back from array elements
        txt = ' '.join(txt)

        clean_txt.append(txt)
    
    # for i in clean_txt:
    #     print(i)
    # print(s_lines)
    # Counter from collections
    lis=[]
    
    word_counts = Counter(str(clean_txt).split(" "))
    lis.append(word_counts)
        #return word_counts
    # n=''
    # c=1
    # for i in clean_txt:
    #     n+=' '
    #     for j in i:

    #         if c>int(fields['word']):
    #             break
    #         else:
    #             n+=j
    #             c=c+1


    print(lis)
    return lis









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
            #print(result)
            if result==[]:
                result=[]
                flash('No records of earthquake for above mentioned days')

        else:
            result=[]
            flash('Please enter values in the field')

        
    return render_template('index.html',data=result)








if __name__ == "__main__":
    app.run()