# A very simple Flask Hello World app for you to get started with...
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home1')
def home1():
    return render_template('home1.html')

@app.route('/home2')
def home2():
    return render_template('home2.html')

@app.route('/home3')
def home3():
    return render_template('home3.html')
@app.route('/home4')
def home4():
    return render_template('home4.html')

@app.route('/bootstrap',methods=['GET','POST'])
def bootstrap():
    return render_template('bootstrap.html')
