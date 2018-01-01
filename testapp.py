from flask import Flask, current_app, request, flash,redirect,url_for,render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = 'secret'
app.config['MONGO_HOST'] = '192.168.99.100'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'testdb'
mongo = PyMongo(app, config_prefix='MONGO')


@app.route('/', methods=['GET'])
def show_entry():

    users = mongo.db.user.find()
    entries = []
    for row in users:
        entries.append(row)

    return render_template('toppage.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    mongo.db.user.insert({"name": request.form['name'], "birthday": request.form['birthday']})
    flash('New entry was successfully posted')
    return redirect(url_for('show_entry'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')

