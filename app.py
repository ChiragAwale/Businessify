from flask import Flask, render_template
import  serviceLayer.capital_one.merchant_data as merchant_data
import config_k as config
from serviceLayer.mapbox import isochrone as isochrone
import serviceLayer.data_handler as dh


app = Flask(__name__)

data_handler = dh.DataHandler()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    #merchants = merchant_data.get_merchants()
    data = merchant_data.get_merchants_capital_one_json()
    isc = isochrone.get_coordinates('-77.042090', '38.903400')

    access_token = config.MAPBOX_ACCESS_TOKEN
    print(access_token)
    return render_template('map-mapbox.html',  data = data, ACCESS_TOKEN = access_token, isc = isc )


@app.route('/map1')
def map1():
    data = data_handler.get_list_by_city("Vaughan")
    print("hi")
    print(data)
    isc = isochrone.get_coordinates('-77.042090', '38.903400')

    access_token = config.MAPBOX_ACCESS_TOKEN

    return render_template('map-google.html',  data=data, ACCESS_TOKEN=access_token, isc=isc )




if __name__ == '__main__':
    app.run()

