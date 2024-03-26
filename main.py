from flask import Flask, render_template


app = Flask(__name__)


# http://www.domena.hr/
@app.route('/')
def index():
    return render_template('index.html')


# http://www.domena.hr/about
@app.route('/about')
def about():
    return render_template('about.html')





if __name__ == '__main__':
    app.run(debug=True)


# smart-key-flask