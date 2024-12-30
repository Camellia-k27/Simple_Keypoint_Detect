from flask import Flask, render_template, request, jsonify
import os
import logging
import json

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_json', methods=['POST'])
def save_json():
    data = request.json
    file_name = data['file_name']
    json_data = data['json_data']
    
    # 定義保存JSON文件的目錄
    save_dir = '/content/data/labels'
    os.makedirs(save_dir, exist_ok=True)
    
    # 保存JSON文件
    with open(os.path.join(save_dir, file_name), 'w') as json_file:
        json.dump(json_data, json_file)
    
    return jsonify({"message": "JSON file saved successfully!"})

if __name__ == '__main__':
app.run(debug=False)

