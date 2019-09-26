from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail


app = Flask(__name__ )

ENV = 'prod'
# development
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:quickerpay@localhost/feedback_db'
else:
    # production
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://avmwehxerlpfgv:015708fac78a9c8976a19fcd8cd3b20e5174b876e29be855966f0b4d6d3208af@ec2-54-83-55-122.compute-1.amazonaws.com:5432/d5i1jioovf89ca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database object
db = SQLAlchemy(app)


# Database model
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())


# Feedback Constructor
def __init__(self, customer, dealer, rating, comments):
    self.customer = customer
    self.dealer = dealer
    self.rating = rating
    self.comments = comments


@app.route('/')
def index():
     return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == "" or dealer == "":
            return render_template('index.html', message="Please enter required fields")
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer= customer, dealer =dealer, rating=rating, comments= comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message="You have already submitted a feedback")


if __name__ == '__main__':
    app.run()
