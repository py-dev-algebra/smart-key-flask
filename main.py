from flask import Flask, render_template

from services.user_services import UserServices



app = Flask(__name__)


# http://www.domena.hr/
@app.route('/')
def index():
    user = UserServices().get_user()
    
    return render_template('index.html', user=user)


# http://www.domena.hr/about
@app.route('/about')
def about():
    return render_template('about.html')





if __name__ == '__main__':
    app.run(debug=True)
