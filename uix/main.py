from flask import Flask, render_template, request
import vanilla.uix.tasks
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='home'), 200


@app.route('/db_')
def db_():
    with open('metadata_db.json', 'r') as f:
        providers = json.load(f)
    return render_template('db.html', providers=providers, title='database'), 200


@app.route("/providerdetails/<section>")
def providerdetails(section):
    section = request.view_args['section']
    with open('descript_data.json') as f:
        meta = json.load(f)
    if section == 'facebook':
        meta = meta['facebook']
    else:
        meta = meta['webpage']
    return render_template('providerdetails.html', title=section, meta=meta)


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
