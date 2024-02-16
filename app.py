from flask import Flask, render_template, jsonify, request, url_for
from response import getRespons
from waitress import serve
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# CORS(app, origins=['http://example.com', 'http://localhost:5000/chatpage']).

@app.route("/")
def index():
    return jsonify('nothing to see here')

@app.route("/send_message", methods=['POST'])
def send_message():
    text = request.form["message"]
    print(text)
    response = getRespons(text)
    message = {"answer": response}
    print(message)
    return jsonify(message)

if __name__ =="__main__":
    app.run(debug=True, port=4040)
    