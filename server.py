from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = '28c5a395-6ecb-4c59-b074-85c624de0c4f'

@app.route('/api/yandexgpt', methods=['POST'])
def yandexgpt():
    data = request.get_json()
    print(f"Received data: {data}")  # Логирование данных для отладки

    prompt = data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    json_data = {
        'prompt': prompt,
        'max_tokens': 100
    }

    try:
        response = requests.post('gpt://b1gcqjenmkra0ghv92e7/yandexgpt/', headers=headers, json=json_data)
        response.raise_for_status()  # Проверка на HTTP ошибки
        return jsonify(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Логирование HTTP ошибок
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), response.status_code
    except Exception as err:
        print(f"Other error occurred: {err}")  # Логирование других ошибок
        return jsonify({'error': f'Other error occurred: {err}'}), 500

if __name__ == '__main__':
    app.run(port=5000)