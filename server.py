from flask import Flask, send_from_directory, make_response
import os

app = Flask(__name__, static_folder='.')

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    # Securely serve static files without exposing directory structure
    return send_from_directory('.', path)

if __name__ == '__main__':
    print("MochiKey Official Site is running! Target: http://mochikey.com")
    print("Local access: http://localhost:8080")
    # Debug mode disabled for security
    app.run(port=8080, debug=False)
