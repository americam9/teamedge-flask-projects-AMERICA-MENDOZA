from flask import Flask, request, render_template, current_app as app
import requests
from sense_hat import SenseHat
from time import sleep

app = Flask(__name__)
sense = SenseHat()

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/success',methods = ['GET', 'POST'])
def success():
   message = request.form['message']
   name = request.form['name']
   sense.show_message(message + " by " + name
   return render_template("success.html", message = message)



if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')