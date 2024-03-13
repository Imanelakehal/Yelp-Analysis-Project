from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@192.168.26.129:3306/metastore'
db = SQLAlchemy(app)

# Define your model for the reviews table
class Review(db.Model):
    __tablename__ = 'review_counts'
    rev_year = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

# Route for the home page
@app.route('/')
def render_website():
    return render_template('index.html')

# Route for the reviews page
@app.route('/templatesReviews.html')
def reviews():
    # Query the database to retrieve data from the reviews table
    data = Review.query.order_by(Review.rev_year.asc()).all()
    return render_template('Reviews.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)