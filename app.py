from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql


pymysql.install_as_MySQLdb()

app = Flask(__name__, static_url_path='/static')

# Connect to the first MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@192.168.26.129:3306/metastore'
db = SQLAlchemy(app)

# Connect to the second MySQL database
app.config['SQLALCHEMY_BINDS'] = {
    'users': 'mysql://root:imane@192.168.56.106:3306/users'
}
app.config['SQLALCHEMY_ECHO'] = True
# Define your models for the first database
class Review(db.Model):
    __tablename__ = 'review_counts'
    rev_year = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

# Define your models for the second database
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

class ReviewSummary(db.Model):
    __tablename__ = 'review_summary'
    rev_year = db.Column(db.Integer, primary_key=True)
    rev_cool_sum = db.Column(db.Integer)
    rev_useful_sum = db.Column(db.Integer)
    rev_funny_sum = db.Column(db.Integer)

class WordCount(db.Model):
    __tablename__ = 'word_ranking'
    word = db.Column(db.String(50), primary_key=True)
    count = db.Column(db.Integer)

# Route for the home page
@app.route('/')
def render_website():
    return render_template('index.html')

# Route for the reviews page
@app.route('/templatesReviews.html')
def reviews():
    # Query data from all three tables
    review_data = Review.query.order_by(Review.rev_year.asc()).all()
    summary_data = ReviewSummary.query.order_by(ReviewSummary.rev_year.asc()).all()
    word_ranking_data = WordCount.query.order_by(WordCount.count.desc()).limit(10).all()

    # Pass data to the template
    return render_template('Reviews.html', review_data=review_data, 
                           summary_data=summary_data, word_ranking_data=word_ranking_data)

# Route for the users page
@app.route('/Users.html')
def users():
    # Query the database to retrieve data from the users table
    users_data = User.query.all()
    return render_template('Users.html', users_data=users_data)

if __name__ == '__main__':
    app.run(debug=True)
