from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello, world! Your server is running.",
        "status": "success"
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "ok",
        "uptime": "running"
    })

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=8083)
