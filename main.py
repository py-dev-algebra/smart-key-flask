from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

from services.user_services import UserServices
from models.users import User



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yekuc60n6T2lgumg7y40mIXhGQw9YKCul2f6OuTDm51e09dGNO5s9Wakh7aX58Iibvbq0Y37Q1Ns204YypgoNxn3610a1agfiUtA'


class UserCreateForm(FlaskForm):
    first_name = StringField('Ime', validators=[DataRequired('Ovo polje je obvezno'), Length(max=50, message='Maksimalno 50 znakova')])
    last_name = StringField('Prezime', validators=[DataRequired('Ovo polje je obvezno'), Length(max=100, message='Maksimalno 100 znakova')])
    pin_code = StringField('PIN', validators=[DataRequired('Ovo polje je obvezno'), Length(min=4, max=4, message='Mora biti tsno 4 znaka')])
    is_active = BooleanField('Aktivan?')
    submit = SubmitField('Snimi')



# http://www.domena.hr/
@app.route('/')
def index():
    users = UserServices().get_users()
    
    return render_template('index.html', users=users)


# http://www.domena.hr/about
@app.route('/about')
def about():
    return render_template('about.html')


# http://www.domena.hr/create-user
@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    user_form = UserCreateForm()

    if user_form.is_submitted():
        user_first_name = user_form.first_name.data
        user_last_name = user_form.last_name.data
        user_pin_code = user_form.pin_code.data
        user_is_active = user_form.is_active.data
        print(user_first_name, user_last_name, user_pin_code, user_is_active)
        UserServices.create_user(User(user_first_name, user_last_name, user_pin_code, user_is_active))
        return redirect(url_for('index'))

    return render_template('create-user.html', form=user_form)



# http://www.domena.hr/edit-user
@app.route('/edit-user', methods=['GET', 'POST'])
def edit_user():
    user_form = UserCreateForm()

    if request.method == 'GET':
        user_form.first_name.data = 'Pero'
        user_form.last_name.data = 'Peric'
        user_form.pin_code.data = '1234'
        user_form.is_active.data = True

    if user_form.is_submitted():
        user_first_name = user_form.first_name.data
        user_last_name = user_form.last_name.data
        user_pin_code = user_form.pin_code.data
        user_is_active = user_form.is_active.data
        print(user_first_name, user_last_name, user_pin_code, user_is_active)
        UserServices.create_user(User(user_first_name, user_last_name, user_pin_code, user_is_active))
        return redirect(url_for('index'))

    return render_template('edit-user.html', form=user_form)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
