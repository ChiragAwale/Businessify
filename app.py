from flask import Flask, render_template
import  serviceLayer.capital_one.merchant_data as merchant_data
import config_k as config
from serviceLayer.mapbox import isochrone as isochrone

app = Flask(__name__)

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



if __name__ == '__main__':
    app.run()

