from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import pymysql
from sqlalchemy.sql import func, desc

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# business's mysql
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:imane@192.168.56.106:3306/users'

db = SQLAlchemy(app)

@app.route('/')
def index():
   return render_template('index.html')
@app.route('/Users.html')
def users_page():
    total_users_count = total_users()
    yearly_growth = calculate_yearly_growth()
    popular_users = get_most_popular_users()
    total_review_count = total_reviews()
    return render_template('Users.html',total_users=total_users_count,yearly_growth=yearly_growth, popular_users=popular_users, total_reviews= total_review_count)
# Function to calculate the total review count
def total_reviews():
    total_review_count = db.session.query(func.sum(User.user_review_count)).scalar()
    return total_review_count

''''''''''''''''''''''''''''''''''''' users analysis'''''''''''''''''''''''''''''''''''''
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Text, primary_key=True)
    user_name = db.Column(db.Text)
    user_review_count = db.Column(db.Integer)
    user_yelping_since = db.Column(db.Text)
    user_useful = db.Column(db.Integer)
    user_funny = db.Column(db.Integer)
    user_cool = db.Column(db.Integer)
    user_fans = db.Column(db.Integer)
    user_elite = db.Column(db.Text)
    user_average_stars = db.Column(db.Float)
    user_compliment_hot = db.Column(db.Integer)
    user_compliment_more = db.Column(db.Integer)
    user_compliment_profile = db.Column(db.Integer)
    user_compliment_cute = db.Column(db.Integer)
    user_compliment_list = db.Column(db.Integer)
    user_compliment_note = db.Column(db.Integer)
    user_compliment_plain = db.Column(db.Integer)
    user_compliment_cool = db.Column(db.Integer)
    user_compliment_funny = db.Column(db.Integer)
    user_compliment_writer = db.Column(db.Integer)
    user_compliment_photos = db.Column(db.Integer)

''''''''''''''''''''''''''''''''''''' review analysis'''''''''''''''''''''''''''''''''''''
class Review(db.Model):
    __tablename__ = 'review_counts'
    rev_year = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

class ReviewSummary(db.Model):
    __tablename__ = 'review_summary'
    rev_year = db.Column(db.Integer, primary_key=True)
    rev_cool_sum = db.Column(db.Integer)
    rev_useful_sum = db.Column(db.Integer)
    rev_funny_sum = db.Column(db.Integer)

class WordCount(db.Model):
    __tablename__ = 'word_count_table'
    word = db.Column(db.String(50), primary_key=True)
    count = db.Column(db.Integer)






# Function to calculate the yearly growth of user sign-ups
def calculate_yearly_growth():
    # Retrieve the earliest and latest sign-up dates
    earliest_date = db.session.query(func.min(User.user_yelping_since)).scalar()
    latest_date = db.session.query(func.max(User.user_yelping_since)).scalar()

    # Calculate the year of sign-up for the earliest and latest dates
    earliest_year = int(earliest_date.split('-')[0])
    latest_year = int(latest_date.split('-')[0])

    # Create a dictionary to store the yearly growth
    yearly_growth = {}

    # Calculate the user count for each year
    for year in range(earliest_year, latest_year + 1):
        year_count = User.query.filter(User.user_yelping_since.like(f'{year}%')).count()
        yearly_growth[year] = year_count

    return yearly_growth


# Function to retrieve the most popular users based on the number of reviews
def get_most_popular_users(limit=10):
    # Query the database to retrieve the users ordered by the number of reviews in descending order
    popular_users = User.query.order_by(desc(User.user_review_count)).limit(limit).all()
    return popular_users


@app.route('/Users.html')
def total_users():
    total_users = User.query.count()
    return f"Total Users: {total_users}"

''''''''''''''''''''''''''''''''''''' users analysis'''''''''''''''''''''''''''''''''''''
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