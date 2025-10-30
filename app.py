from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({
        "status": "QuSecure-Mail Server Running", 
        "version": "1.0",
        "modules": ["Flask", "AI Entropy", "PQC Crypto"]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
