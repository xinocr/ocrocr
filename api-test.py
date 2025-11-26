import base64
import requests

def predict_image(image_path, question_type):
    with open(image_path, 'rb') as f:
        image_data = f.read()

    payload = {
        'base64Image': base64.b64encode(image_data).decode('utf-8'),
        'modelName': '普通模型',
        'keyCode': '您的keyCode',
        'question': question_type,
        'system': ''
    }

    response = requests.post('http://gpu1.xinyuocr.xyz:8889/api/qrcode/predict', json=payload)
    return response.json()

# 使用示例
image_path = 'path/to/your/image.jpg'
question_type = '框出正确位置'  # 或 '识别图中文本' // 仅支持英文和数字' 或 '回答图中问题'
result = predict_image(image_path, question_type)
print(result)
