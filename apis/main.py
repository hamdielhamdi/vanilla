from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/list')
def access_list():
    return jsonify({'@reponse': 'api list'}), 200


@app.route('/bydate')
def get_by_date():
    global from_, to_
    try:
        from_ = request.args['from']
        to_ = request.args['to']
    except Exception :
        return jsonify({'@response':'invalid query'}), 404
    return from_, to_


if __name__ == '__main__':
    app.run()