from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Update the SQLAlchemy configuration with the correct MySQL URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:imane@192.168.56.106:3306/users'
# Assuming MySQL server is running locally
db = SQLAlchemy(app)

# Define your User model
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255))

@app.route('/')
def index():
    # Fetch all users from the database
    total_users = User.query.all()
    return render_template('index.html', total_users=total_users)

if __name__ == '__main__':
    app.run(debug=True)
