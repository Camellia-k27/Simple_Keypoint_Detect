from flask import Flask, render_template, request, jsonify
import os
import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':

    app.run(debug=False)
