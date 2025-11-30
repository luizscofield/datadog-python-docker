from flask import Flask
import time
import requests

app = Flask(__name__)

@app.route('/')
def health_check():
    return "OK", 200

@app.route('/process')
def process():
    time.sleep(0.2)
    return "Processed by App B", 200

@app.route('/long_request')
def long_request():
    response = requests.get("http://python-app-c:5000/process")
    return f"App C says: {response.text}", response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
