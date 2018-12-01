from flask import Flask, render_template, send_from_directory,flash, session, request
from businessify import service_layer as merchant_data, service_layer as dh, config_k as config
from businessify.service_layer import isochrone as isochrone
import os

app = Flask(__name__)


data_handler = dh.DataHandler()


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




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)
