from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.static_folder = 'static'  # Set static folder path

# Route for the home page
@app.route('/')
def render_website():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
