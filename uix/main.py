from flask import Flask, render_template, request
from vanilla.v2.db.database import get,connect
import vanilla.uix._ as tools
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='home'), 200



@app.route('/db_')
def db_():
    providers = tools.providers()
    return render_template('db.html', providers=providers, title='database'), 200


@app.route("/providerdetails/<section>")
def providerdetails(section):
    section = request.view_args['section']
    data = get(connect('localhost',27017),section)
    metadata = []
    for i in data:
        metadata.append(i.keys())

    return render_template('providerdetails.html',data=data[0:5], title=section, keys=list(metadata[0]))

if __name__ == '__main__':
    app.run(debug=True)
