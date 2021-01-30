from flask import Flask, render_template, request, json, jsonify
import os 

app = Flask(__name__, static_folder="static")


@app.route('/api/v1/movies', methods=['GET'])
def movies_json():
    movies_info = os.path.join(app.static_folder, 'data', 'movies.json')
    with open(movies_info, 'r') as json_data:
        json_info = json.load(json_data)
    return jsonify(json_info)

@app.route('/api/v1/movies/clean', methods=['GET'])
def movies_clean():
    results = []
    movies_info = os.path.join(app.static_folder, 'data', 'movies.json')
    with open(movies_info, 'r') as json_data:
        json_info = json.load(json_data)
    for movie in json_info:
        results.append(movie)

    return render_template('movies.html', results=results)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')