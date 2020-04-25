from flask import Flask, render_template, request, redirect, url_for
import flask_login
import dash
import dash_html_components as html
import pandas as pd
import numpy as np
import json

login_manager = flask_login.LoginManager()

application = Flask(__name__)

application.secret_key = 'k@2C#DGtOP#qO$;N6wUvXv3$:O/SpL'  # Change in production. Generated with Fort Knox
login_manager.init_app(application)


# Users
# People, companies, investors

# Mockup DB
users = {'abc@d.io':
             {'password': 'secret'}
         }

# USER CLASS
class User(flask_login.UserMixin):
    pass

# def company_similarity()

#     return sim_company

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user


@application.route('/')
def index():
    return render_template("index.html")

@application.route('/register_com')
def register_com():
    return render_template("register_com.html")

@application.route('/register_person')
def register_person():
    return render_template("register_person.html")
#
@application.route('/register_investor')
def register_investor():
    return render_template("register_investor.html")


# applicant_person
# @app.route('/')
# def index():
#     return render_template("index.html")
# applicant_company

# applicant_investor

# LOGIN
@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

        # return '''
        #        <form action='login' method='POST'>
        #             <input type='text' name='email' id='email' placeholder='email'/>
        #             <input type='password' name='password' id='password' placeholder='password'/>
        #             <input type='submit' name='submit'/>
        #        </form>
        #        '''

    email = request.form['email']
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'

# LOGOUT
@application.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@application.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

# def calc_similarity(arg)



if __name__ == '__main__':
    application.run()
