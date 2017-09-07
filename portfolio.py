from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def rootRoute():
    return render_template('index.html')

@app.route('/projects')
def projectRoute():
    return render_template('projects.html')

@app.route('/about')
def aboutRoute():
    return render_template('about.html')

app.run(debug=True)
