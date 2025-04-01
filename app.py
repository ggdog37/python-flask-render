# 啟動 python app.py
# 中止 Ctrl + C
# 清除 Clear
from flask import Flask, jsonify,render_template
import random

app = Flask(__name__)

@app.route('/get_hrv', methods=['GET'])
def get_hrv():
    # 模擬 HRV 數據（可以改為真實的數據來源）
    hrv = random.uniform(30.0, 100.0)  # 隨機生成一個 HRV 數據
    return jsonify({'hrv': hrv})

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
