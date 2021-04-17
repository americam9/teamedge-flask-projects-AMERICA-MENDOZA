from flask import Flask, request, render_template, current_app as app
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
   conn = sqlite3.connect('./static/data/senseDisplay.db')
   curs = conn.cursor()
   curs.execute("INSERT INTO messages (name, message) VALUES((?),(?))",(name, message))
   conn.commit()
   conn.close()
   sense.show_message(message)
   return render_template("success.html", message = message)

@app.route('/all')
def all():
    conn = sqlite3.connect('./static/data/senseDisplay.db')
    curs = conn.cursor()
    messages = []
    rows = curs.execute("SELECT * from messages")
    for row in rows:
        message = {'name': row[0], 'message':row[1]}
        messages.append(message)
    conn.close()
    return render_template('stormform.html', messages = messages)


if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')
