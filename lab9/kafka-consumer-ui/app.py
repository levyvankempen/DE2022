from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# check the following article if you want to know more about SQLAlchemy and Flask
# https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wordcounts.sqlite3'
db = SQLAlchemy(app)

from models import Wordcount

with app.app_context():
    db.create_all()


@app.route('/')
def show_all():
    return render_template('show_all.html', wordcounts=Wordcount.query.all())


from consumer import KafkaMessageConsumer

KafkaMessageConsumer()
app.run(host='0.0.0.0', port=5000, debug=True)
