from flask import Flask, render_template
import  serviceLayer.captialOne.merchant_data as merchant_data
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    merchants = merchant_data.get_merchants()
    data = merchant_data.get_merchants_json()
    return render_template('map.html',merchants = merchants[:10], data = data)



if __name__ == '__main__':
    app.run()

