import requests

# URL của API đã deploy trên Render
url = "https://web-vulnerabilities-detection/predict"

# Tập dữ liệu test
test_data = [
    {"features": [0.5, 1.2, 3.4, 0.1]},
    {"features": [0.8, 1.0, 2.3, 0.5]},
    {"features": [1.1, 0.3, 1.5, 0.7]}
]

# Lặp qua từng dữ liệu test và gửi request
for idx, data in enumerate(test_data):
    try:
        # Gửi request POST tới API
        response = requests.post(url, json=data)
        
        # In kết quả
        print(f"Test case {idx + 1}:")
        print(f"Input: {data['features']}")
        if response.status_code == 200:
            print(f"Output: {response.json()}\n")
        else:
            print(f"Error: {response.status_code} - {response.text}\n")
    except Exception as e:
        print(f"Test case {idx + 1} failed with error: {str(e)}\n")

if response.json()['prediction'][0] == 0:
    print("✅ Input này không phải là lỗ hổng.")
else:
    print("⚠️ Input này là lỗ hổng. Đề xuất kiểm tra thêm.")
