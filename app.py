from flask import Flask, render_template, send_from_directory,flash,redirect,session,abort,request
import  service_layer.capital_one.merchant_data as merchant_data
import config_k as config
from service_layer import isochrone as isochrone
import service_layer.data_handler as dh
import os
from sqlalchemy.orm import sessionmaker
from data_layer.tabledef import *


app = Flask(__name__)

data_handler = dh.DataHandler()


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"


@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route('/map')
def map():
    #merchants = merchant_data.get_merchants()
    data = merchant_data.get_merchants_capital_one_json()
    isc = isochrone.get_isochrone_mapbox('-77.042090', '38.903400')

    access_token = config.MAPBOX_ACCESS_TOKEN
    print(access_token)
    return render_template('map-mapbox.html',  data = data, ACCESS_TOKEN = access_token, isc = isc )


@app.route('/map1')
def map1():
    data = data_handler.get_list_by_city("Vaughan")
    isc = isochrone.get_isochrone_os('38.903400','-77.042090' )
    access_token = config.MAPBOX_ACCESS_TOKEN

    return render_template('map-google.html',   data=data, ACCESS_TOKEN=access_token, isc=isc )


@app.route('/service_layer/data/dataset.json')
def da():
    return send_from_directory("service_layer/data/","dataset.json")




app.secret_key = os.urandom(12)
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)
