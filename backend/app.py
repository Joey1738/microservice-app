from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status="Backend healthy"), 200

@app.route('/api/data')
def data():
    return jsonify(message="Hello from Backend!", data=[1, 2, 3]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
