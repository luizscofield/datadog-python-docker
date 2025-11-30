from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def health_check():
    return "OK", 200

@app.route('/call-b')
def call_service_b():
    response = requests.get("http://python-app-b:5000/process")
    return f"Service B says: {response.text}", response.status_code

@app.route('/long_request')
def long_request():
    response = requests.get("http://python-app-b:5000/long_request")
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
