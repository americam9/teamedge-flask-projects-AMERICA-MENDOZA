from flask import Flask 
from flask_apscheduler import APScheduler
from sensehat import SenseHat

app = Flask(__name__)
scheduler.init_app(app)
scheduler.start()

scheduler.add_job(id=unique_string_rowid, func=name name_of_function_you_want_to_run, 
trigger= 'date', run_date= string_date_time_when_function_should_run, args = [any_arguments_
you_want_to_pass_to_the_func]) 

def show_reminder(reminder):

