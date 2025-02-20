from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load mô hình
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "AI Model Deployment with Flask on Render!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Lấy dữ liệu từ request
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)  # Chuyển thành mảng 2D
        prediction = model.predict(features)  # Dự đoán
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
