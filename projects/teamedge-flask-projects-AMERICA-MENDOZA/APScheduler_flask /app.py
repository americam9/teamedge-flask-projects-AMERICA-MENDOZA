from flask import Flask 
from flask_apscheduler import APScheduler
from sensehat import SenseHat

app = Flask(__name__)
scheduler.init_app(app)
scheduler.start()

@app.route('/send', methods= ['POST'])
def inserttask():
    task = request.form['task']
    date = request.form['date']
    due = request.form['due']
    display = task + "sumbitted: " + date + "due by: " + due
    sense.show_message(display)
    return render_template('inserttask.html', task=task, date=date, due=due)

