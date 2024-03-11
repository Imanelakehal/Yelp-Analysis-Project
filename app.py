from flask import Flask, render_template, send_from_directory, redirect, url_for

app = Flask(__name__)
app.static_folder = 'static'  # Set static folder path

# Route for the home page
@app.route('/')
def render_website():
    return render_template('index.html')

@app.route('/businesses')
def page1():
    return render_template('businesses.html')

@app.route('/Users')
def page2():
    return render_template('Users.html')


if __name__ == '__main__':
    app.run(debug=True)
