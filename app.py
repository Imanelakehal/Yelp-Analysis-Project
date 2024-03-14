from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to the first MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@192.168.26.129:3306/metastore'
db = SQLAlchemy(app)

# Connect to the second MySQL database
app.config['SQLALCHEMY_BINDS'] = {'users': 'mysql://root:imane@192.168.56.106:3306/users'}

# Define your models for the first database
class Review(db.Model):
    __bind_key__ = 'default'
    __tablename__ = 'review_counts'
    rev_year = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

# Define your models for the second database
class User(db.Model):
    __bind_key__ = 'users'
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

# Route for the home page
@app.route('/')
def render_website():
    return render_template('index.html')

# Route for the reviews page
@app.route('/reviews')
def reviews():
    # Query the database to retrieve data from the reviews table
    data = Review.query.order_by(Review.rev_year.asc()).all()
    return render_template('Reviews.html', data=data)

############################################################### Users Page ###############################################################

# Route for the users page
@app.route('/users/')
def users():
    # Query the database to retrieve data from the users table
    users_data = User.query.all()
    return render_template('Users.html', users_data=users_data)

if __name__ == '__main__':
    app.run(debug=True)
