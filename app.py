from flask import Flask, render_template, request, jsonify
import json
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({"status": "QuSecure-Mail Server Running"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
