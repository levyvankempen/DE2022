from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wordcounts.sqlite3'
db = SQLAlchemy(app)


class Wordcount(db.Model):
    word = db.Column('word', db.String, primary_key=True)
    count = db.Column('count', db.Integer)


@app.route('/')
def show_all():
    return render_template('show_all.html', wordcounts=Wordcount.query.all())


if __name__ == '__main__':
    from consumer import KafkaMessageConsumer

    db.create_all()
    KafkaMessageConsumer()
    app.run(host='0.0.0.0', port=5000, debug=True)
