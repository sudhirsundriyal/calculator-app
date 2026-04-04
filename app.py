# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    # Numbers from command-line arguments
    import sys
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except (IndexError, ValueError):
        a = 10
        b = 20
    sum_result = a + b
    return jsonify({"message": "Calculator app is running...", "sum": sum_result})

if __name__ == '__main__':
    # Bind on all interfaces so container is accessible externally
    app.run(host='0.0.0.0', port=80)
