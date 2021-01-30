from flask import Flask, render_template,
current_app as app

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Americas Rainbow Project"

@app.route('/red')
def red.html():
    return render_template('red.html')

@app.route('/orange')
def orange.html():
    return render_template('orange.html')

@app.route('/yellow')
def yellow.html():
    return render_template('yellow.html')

@app.route('/green')
def green.html():
    return render_template('green.html')

@app.route('/blue')
def blue.html():
    return render_template('blue.html')

@app.route('/indigo')
def indigo.html():
    return render_template('indigo.html')

@app.route('/violet')
def violet.html():
    return render_template('violet.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

