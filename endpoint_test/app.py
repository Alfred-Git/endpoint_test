from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/check', methods=['GET'])
def check():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
