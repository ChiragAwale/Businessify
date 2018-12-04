from flask import render_template, url_for, flash, redirect, request,send_from_directory, jsonify
from businessify import app, db, bcrypt
from businessify.forms import RegistrationForm, LoginForm
from businessify.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import businessify.service_layer.capital_one.merchant_data as merchant_data
import businessify.config_k as config, businessify.service_layer.data_handler as dh
from businessify.service_layer import isochrone as isochrone
import os


data_handler = dh.DataHandler()




@app.route("/home")
def home():
    data = data_handler.get_list_by_state("ON")
    isc = isochrone.get_isochrone_os('38.903400', '-77.042090')
    access_token = config.MAPBOX_ACCESS_TOKEN
    return render_template('analyze.html', data=data, ACCESS_TOKEN=access_token, isc1=isc[0],isc2 = isc[1], isc10 = isc[2
    ])

@app.route("/analyze", methods = ['POST','GET'])
def analyze():
    name = request.form["name"]
    type = request.form["type"]
    location = request.form["address"]
    data = data_handler.get_list_by_category(type)
    isc = data_handler.get_isochrone(location)
    return render_template('analyze.html', data=data,isc1=isc[0],isc2 = isc[1], isc10 = isc[2], title = name)



@app.route("/background_get_isochrone", methods =['POST','GET'])
def background_test():
    print("test")
    location = request.form["place"]
    isc = data_handler.get_isochrone(location)
    print("Returned")
    print(isc)
    return jsonify(isc_data = isc)

@app.route("/background_get_cluster", methods =['POST','GET'])
def background_get_cluster():
    print("cluster test")
    state = request.form["state"]
    cluster_data = data_handler.get_list_by_state(state)
    print("Returned")
    print(cluster_data)
    return cluster_data

@app.route("/")
@app.route("/analyze_form")
def analyze_form():
    return render_template('analyze_form.html', title='Analyze')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')



@app.route('/map')
def map():
    #merchants = merchant_data.get_merchants()
    data = merchant_data.get_merchants_capital_one_json()
    isc = isochrone.get_isochrone_mapbox('-77.042090', '38.903400')

    access_token = config.MAPBOX_ACCESS_TOKEN
    print(access_token)
    return render_template('map-mapbox.html', data = data, ACCESS_TOKEN = access_token, isc = isc)


@app.route('/map1')
def map1():
    data = data_handler.get_list_by_city("Vaughan")
    isc = isochrone.get_isochrone_os('38.903400', '-77.042090')
    access_token = config.MAPBOX_ACCESS_TOKEN

    return render_template('map-google.html', data=data, ACCESS_TOKEN=access_token, isc=isc)


@app.route('/service_layer/data/dataset.json')
def da():
    return send_from_directory("service_layer/data/","dataset.json")



