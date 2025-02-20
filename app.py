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
        # Lấy dữ liệu JSON từ request
        data = request.get_json()
        
        if 'features' not in data:
            return jsonify({'error': 'Missing features in request'}), 400
        
        features = np.array(data['features']).reshape(1, -1)  # Chuyển về mảng 2D
        prediction = model.predict(features)[0]  # Dự đoán lớp lỗ hổng
        result = vulnerability_classes.get(prediction, 'Unknown Vulnerability')
        
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Lấy cổng từ biến môi trường hoặc mặc định là 5000
    app.run(host='0.0.0.0', port=port, debug=True)
