# 啟動 python app.py
# 中止 Ctrl + C
# 清除 Clear
from flask import Flask, jsonify,render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/get_hrv', methods=['GET'])
def get_hrv():
    # 模擬 HRV 數據（可以改為真實的數據來源）
    hrv = random.uniform(30.0, 100.0)  # 隨機生成一個 HRV 數據
    return jsonify({'hrv': hrv})

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/demo')
def demo():
    return render_template('0401.html')


if __name__ == '__main__':
    app.run(debug=True)
