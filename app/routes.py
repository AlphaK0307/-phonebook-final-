# from re import template
from crypt import methods
from app import app
from flask import redirect, render_template, url_for
from app.forms import SignUpForm, RegisterePhoneForm
from app.models import User, Post

@app.route('/')
def index():
    title='Home'
    user= {'id': 1, 'username':'Patel', 'email':'keyurpatel1121@gmail.com'}
    posts = Post.query.all()
    return render_template('index.html', current_user=user, title=title, posts=posts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    title= 'Sign Up'
    form = SignUpForm()
    if form.validate_on_submit():
        email=form.email.data
        username=form.username.data
        password=form.password.data
        # create new user instance
        new_user=User(email=email,username=username, password=password)
        return redirect(url_for('index'))
    return render_template('signup.html', title=title, form=form)


@app.route('/login')
def login():
    title= 'Login In'
    return render_template('login.html', title=title)


@app.route('/register-phone', methods=["GET", "POST"])
def  register_phone():
    title= 'Register your Phone'
    form= RegisterePhoneForm()
    if form.validate_on_submit():
        first_name=form.first_name.data
        last_name=form.last_name.data
        phone_number=form.phone_number.data
        city=form.city.data
        print(first_name, last_name, phone_number, city)
    return render_template('register_phone.html', title=title, form=form)
