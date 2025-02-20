from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load mô hình Random Forest đã huấn luyện
model = joblib.load('model.pkl')

# Danh sách các lỗ hổng bảo mật
vulnerability_classes = {0: 'CWE-79 (XSS)', 1: 'CWE-80 (XSS)', 2: 'CWE-20 (Improper Input Validation)'}

@app.route('/')
def home():
    return "<h1>Web Vulnerability Detection API</h1><p>Use /predict to get predictions</p>"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Lấy dữ liệu đầu vào từ request
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        # Kiểm tra dữ liệu đầu vào có đúng định dạng không
        if 'features' not in data:
            return jsonify({'error': 'Missing "features" in input data'}), 400
        
        # Dữ liệu phải là list các đặc trưng
        features = data['features']
        prediction = model.predict([features])  # Dự đoán
        
        # Trả về kết quả
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Lấy cổng từ biến môi trường hoặc mặc định là 5000
    app.run(host='0.0.0.0', port=port, debug=True)
