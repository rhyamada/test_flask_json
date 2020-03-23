from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    dados = dict(id=1,data=234)
    return jsonify(dados), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)