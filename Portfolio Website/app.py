from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    message = ""

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        msg = request.form['message']

        message = f"Thank You {username}! Message Received."

    return render_template('contact.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)