from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    body = request.get_json()
    return jsonify({ "result" : body["first"] + body["second"] }), 200 

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    body = request.get_json()
    return jsonify({ "result" : body["first"] - body["second"] }), 200 

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
