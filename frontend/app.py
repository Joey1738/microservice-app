import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    backend_url = os.getenv("BACKEND_URL", "http://backend-service:5001")
    try:
        r = requests.get(f"{backend_url}/api/data")
        data = r.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
