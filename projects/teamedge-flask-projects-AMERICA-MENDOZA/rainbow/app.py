from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Americas Rainbow Project"

@app.route('/red')
def red_html():
    return render_template('red_html')

@app.route('/orange')
def orange_html():
    return render_template('orange_html')

@app.route('/yellow')
def yellow_html():
    return render_template('yellow_html')

@app.route('/green')
def green_html():
    return render_template('green_html')

@app.route('/blue')
def blue_html():
    return render_template('blue_html')

@app.route('/indigo')
def indigo_html():
    return render_template('indigo_html')

@app.route('/violet')
def violet_html():
    return render_template('violet_html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

