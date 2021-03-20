from flask import Flask, request, render_template, current_app as app
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("login.html")

@app.route('/success',methods = ['GET', 'POST'])
def login():
   message = request.form['message']
   name = request.form['name']
   return render_template("success.html", message = message)



if __name__ == '__main__':
   app.run(debug = True)
