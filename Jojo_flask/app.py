from flask import Flask, request, render_template, current_app as app
from sense_hat import SenseHat
from time import sleep

app = Flask(__name__)
sense = SenseHat()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        thought = request.gorm.get("thought")
        sense.show_thought(thought)
   return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
