from flask import Flask, render_template

import vanilla.uix._ as tools

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', title='home'), 200


@app.route('/db_')
def db_():
    providers = tools.providers()
    return render_template('db.html', providers=providers, title='database'), 200




if __name__ == '__main__':
    app.run(debug=True)
