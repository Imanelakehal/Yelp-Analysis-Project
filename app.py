from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import pymysql
from sqlalchemy.sql import func, desc
import json

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# Configuration for connecting to multiple databases
app.config['SQLALCHEMY_BINDS'] = {
    'users': 'mysql://root:imane@192.168.56.106:3306/users',
    'business': 'mysql://root:imane@192.168.56.106:3306/business'
}

db = SQLAlchemy(app)

@app.route('/')
def index():
   return render_template('index.html')

''''''''''''''''''''''''''''''''''''' business analysis'''''''''''''''''''''''''''''''''''''
class Business(db.Model):
    __bind_key__ = 'business'
    __tablename__ = 'business'

    business_id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    postal_code = db.Column(db.String(20))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    stars = db.Column(db.Float)
    review_count = db.Column(db.Integer)



@app.route('/templates\business.html')
def business():
    # Fetch analysis results from the database using SQLAlchemy
    # top 20 merchants in the United States
    top_merchants = db.session.query(Business.name, func.count(Business.name).label('cnt')) \
        .group_by(Business.name) \
        .order_by(func.count(Business.name).desc()) \
        .limit(20) \
        .all()

    # top 10 cities with the most merchants in the United States
    top_cities = db.session.query(Business.city, func.count(Business.city).label('merchant_count')) \
        .group_by(Business.city) \
        .order_by(func.count(Business.city).desc()) \
        .limit(10) \
        .all()

    # top 5 states with the most merchants in the United States
    top_states = db.session.query(Business.state, func.count(Business.state).label('merchant_count')) \
        .group_by(Business.state) \
        .order_by(func.count(Business.state).desc()) \
        .limit(5) \
        .all()

    # Extract state names and merchant counts from the query results
    state_names = [state for state, _ in top_states]
    merchant_counts = [count for _, count in top_states]

    # Create a dictionary with the chart data
    chart_data = {
        'data': [{
            'type': 'bar',
            'x': state_names,
            'y': merchant_counts
        }],
        'layout': {
            'title': 'Top 5 States by Merchant Count',
            'xaxis': {'title': 'State'},
            'yaxis': {'title': 'Merchant Count'}
        }
    }

    # Convert the chart data to JSON format
    chart_data_json = json.dumps(chart_data)

    # Common merchants in the United States and their average rate 
    result = db.session.query(Business.name, func.count(Business.name).label('merchant_count'), func.avg(Business.stars).label('average_rating')) \
        .group_by(Business.name) \
        .order_by(func.count(Business.name).desc()) \
        .limit(20) \
        .all()


    return render_template('business.html', top_merchants=top_merchants, city_analysis=top_cities, chart_data_json=chart_data_json, result=result)

''''''''''''''''''''''''''''''''''''' business analysis'''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''' users analysis'''''''''''''''''''''''''''''''''''''
class User(db.Model):
    __bind_key__ = 'users'
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


''''''''''''''''''''''''''''''''''''' review analysis'''''''''''''''''''''''''''''''''''''
class Review(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'review_counts'
    rev_year = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

class ReviewSummary(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'review_summary'
    rev_year = db.Column(db.Integer, primary_key=True)
    rev_cool_sum = db.Column(db.Integer)
    rev_useful_sum = db.Column(db.Integer)
    rev_funny_sum = db.Column(db.Integer)

class WordCount(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'word_count_table'
    word = db.Column(db.String(50), primary_key=True)
    count = db.Column(db.Integer)

@app.route('/templatesReviews.html')
def reviews():
    # Query data from all three tables
    review_data = Review.query.order_by(Review.rev_year.asc()).all()
    summary_data = ReviewSummary.query.order_by(ReviewSummary.rev_year.asc()).all()
    word_ranking_data = WordCount.query.order_by(WordCount.count.desc()).limit(10).all()

    # Pass data to the template
    return render_template('Reviews.html', review_data=review_data, 
                           summary_data=summary_data, word_ranking_data=word_ranking_data)

''''''''''''''''''''''''''''''''''''' review analysis'''''''''''''''''''''''''''''''''''''


''''''''''''''''''''''''''''''''''''' Checkin analysis'''''''''''''''''''''''''''''''''''''
class YearlyCheckinCount(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'yearly_checkin_count'

    year = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

@app.route('/templatescheckin.html')
def yearly_counts():
    # Query the database to retrieve the yearly counts data
    yearly_counts_data = YearlyCheckinCount.query.all()

    return render_template('checkin.html', yearly_counts_data=yearly_counts_data)

''''''''''''''''''''''''''''''''''''' Checkin analysis'''''''''''''''''''''''''''''''''''''



''''''''''''''''''''''''''''''''''''' Rating analysis'''''''''''''''''''''''''''''''''''''

    





@app.route('/emplatesRating.html')
def rating_distribution():

    return render_template('Rating.html')

''''''''''''''''''''''''''''''''''''' Rating analysis'''''''''''''''''''''''''''''''''''''






@app.route('/templatesabout.html')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)