from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def index():
    return 'Hello World'

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
