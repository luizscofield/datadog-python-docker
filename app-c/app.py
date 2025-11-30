from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def health_check():
    return "OK", 200

@app.route('/process')
def process():
    time.sleep(1)
    return "Processed by App C", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
