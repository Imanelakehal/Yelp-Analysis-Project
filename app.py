from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to the first MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@192.168.26.129:3306/metastore'
db1 = SQLAlchemy(app)

# Connect to the second MySQL database
app.config['SQLALCHEMY_BINDS'] = {
    'users': 'mysql://root:imane@192.168.56.106:3306/users'
}
db2 = SQLAlchemy(app)

# Define your models for the first database
class Review(db1.Model):
    __tablename__ = 'review_counts'
    rev_year = db1.Column(db1.Integer, primary_key=True)
    count = db1.Column(db1.Integer)

# Define your models for the second database
class User(db2.Model):
    __tablename__ = 'users'
    id = db2.Column(db2.Integer, primary_key=True)
    username = db2.Column(db2.String(50), unique=True)

class ReviewSummary(db1.Model):
    __tablename__ = 'review_summary'
    rev_year = db1.Column(db1.Integer, primary_key=True)
    rev_cool_sum = db1.Column(db1.Integer)
    rev_useful_sum = db1.Column(db1.Integer)
    rev_funny_sum = db1.Column(db1.Integer)

class WordCount(db1.Model):
    __tablename__ = 'word_ranking'
    word = db1.Column(db1.String(50), primary_key=True)
    count = db1.Column(db1.Integer)

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


if __name__ == '__main__':
    app.run(debug=True)
