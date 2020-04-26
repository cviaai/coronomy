from flask import Flask, render_template, request, redirect, url_for
import flask_login
from flask_sqlalchemy import SQLAlchemy
import os

login_manager = flask_login.LoginManager()

application = Flask(__name__)

application.secret_key = 'k@2C#DGtOP#qO$;N6wUvXv3$:O/SpL'  # Change in production. Generated with Fort Knox
login_manager.init_app(application)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://u1035123_test:u1035123_test@37.140.192.112/u1035123_default'
db = SQLAlchemy(application)

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

@application.route('/demo_invest')
def demo_invest():
    return render_template("demo_investor.html")

@application.route('/register_investor')
def register_investor():
    return render_template("register_investor.html")

# @application.route('/protected')
# def demo_person():
#     return render_template("demo_person.html")


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
    return render_template("demo_person.html") + flask_login.current_user.id
    # return 'Logged in as: ' + flask_login.current_user.id

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

# def calc_similarity(arg)

class Companies(db.Model):
    companyID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    com_name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    jobs_count = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    social = db.Column(db.String(100), nullable=True)
    skill = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    product = db.Column(db.String(100), nullable=False)
    resources_required = db.Column(db.String(500), nullable=True)
    help = db.Column(db.String(500), nullable=True)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, com_name, surname, jobs_count, phone, email, social, skill, address, product,
                 resources_required, help, password):
        self.com_name = com_name
        self.surname = surname
        self.jobs_count = jobs_count
        self.phone = phone
        self.email = email
        self.social = social
        self.skill = skill
        self.address = address
        self.product = product
        self.resources_required = resources_required
        self.help = help
        self.password = password


com_keys = ["com_name", "surname", "jobs_count", "phone", "email", "social", "skill", "address",
                "product", "resources_required", "help", "password"]

mandatory_com_keys = ["com_name", "surname", "jobs_count", "phone", "email", "skill", "address",
                "product", "resources_required", "password"]
# endpoint to create a new user
@application.route("/reg_com", methods=['GET', 'POST'])
def add_company():
    rf = request.form

    empty = False
    field = None
    for el in mandatory_com_keys:
        if not rf[el]:
            empty = True
            field = el
    if empty:
        return "<html><head></head><body>Please enter the necessary field " + field + "</body></html>"

    params = {}
    values = []
    for i in range(len(com_keys)):
        try:
            values.append(rf[com_keys[i]])
        except:
            print("An exception occurred: " + str(com_keys[i]))
            print("An exception occurred: " + str(rf[com_keys[i]]))
    print(values)
    i = 0
    for kk in com_keys:
        params.update({kk: values[i]})
        i += 1
    print(params)

    company = Companies(**params)
    db.session.add(company)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
    return "<html><head></head><body>'Record successfully added'</body></html>"


class Employees(db.Model):
    employeeID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    social = db.Column(db.String(100), nullable=True)
    profession = db.Column(db.String(100), nullable=False)
    education = db.Column(db.Integer, nullable=False)
    skill = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    previous = db.Column(db.String(100), nullable=False)
    infos = db.Column(db.String(500), nullable=True)
    ready = db.Column(db.Integer, nullable=False)
    help = db.Column(db.String(500), nullable=True)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, name, surname, age, phone, email, social, profession, education, skill, address, previous,
                 infos, ready, help, password):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.email = email
        self.social = social
        self.profession = profession
        self.education = education
        self.skill = skill
        self.address = address
        self.previous = previous
        self.infos = infos
        self.ready = ready
        self.help = help
        self.password = password


emp_keys = ["name", "surname", "age", "phone", "email", "social", "profession", "education", "skill", "address",
                "previous", "infos", "ready", "help", "password"]

mandatory_emp_keys = ["name", "surname", "age", "phone", "email", "profession", "education", "skill", "address",
                     "previous", "ready", "password"]

# endpoint to create a new user
@application.route("/reg_person", methods=['GET', 'POST'])
def add_user():
    rf = request.form

    empty = False
    field = None
    for el in mandatory_emp_keys:
        if not rf[el]:
            empty = True
            field = el
    if empty:
        return "<html><head></head><body>Please enter the necessary field " + field + "</body></html>"

    params = {}
    values = []
    for i in range(len(emp_keys)):
        try:
            values.append(rf[emp_keys[i]])
        except:
            print("An exception occurred: " + str(emp_keys[i]))
            print("An exception occurred: " + str(rf[emp_keys[i]]))
    print(values)
    i=0
    for kk in emp_keys:
        params.update({kk : values[i]})
        i+=1
    print(params)

    employee = Employees(**params)

    db.session.add(employee)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
    return "<html><head></head><body>'Record successfully added'</body></html>"

    #   render_template('index.html')

if __name__ == '__main__':
    application.run()
