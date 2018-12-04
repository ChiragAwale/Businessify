import businessify.service_layer.helper as helper
import json
import businessify.service_layer.isochrone as isochrone_service
import businessify.config_k as config
import requests
class DataHandler:

    def __init__(self):
        self.df = helper.read_djson()

    def get_list_by_city(self,city):
        dt = self.df[self.df['city'].isin([city])]
        d = dt.to_dict(orient='records')
        j = json.dumps(d)
        return j

    def get_list_by_category(self, category):
        dt = self.df.where(self.df['categories'].str.contains(category) != None)
        d = dt.to_dict(orient='records')
        j = json.dumps(d)
        return j


    def get_list_by_state(self,state):
        dt = self.df[self.df['state'].isin([state])]
        d = dt.to_dict(orient='records')
        j = json.dumps(d)
        return j

    # Converts given DataFrame to  GeoJson for map
    def df_to_geojson(self, properties, lat='latitude', lon='longitude',df=None):
        df = self.df
        geojson = {'type': 'FeatureCollection', 'features': []}
        for _, row in df.iterrows():
            feature = {'type': 'Feature',
                       'properties': {},
                       'geometry': {'type': 'Point',
                                    'coordinates': []}}
            feature['geometry']['coordinates'] = [row[lon], row[lat]]
            for prop in properties:
                feature['properties'][prop] = row[prop]
            geojson['features'].append(feature)
        return geojson

    def get_isochrone(self, location):
        position = helper.get_geocode(location)
        lat = position["lat"]
        lng = position["lng"]
        return isochrone_service.get_isochrone_os(lat,lng)

    def get_geocode(location):
        request_url = "https://maps.googleapis.com/maps/api/geocode/json?" \
                      "address=" + location + \
                      "&key=" + config.GOOGLEMAP_API
        # print(request_url)
        resp = requests.get(request_url)
        json_object = resp.json()
        # print(json_object["results"][0]["geometry"]["location"])
        return json_object["results"][0]["geometry"]["location"]