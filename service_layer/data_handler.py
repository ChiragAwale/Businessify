import service_layer.helper as helper
import json

class DataHandler:

    def __init__(self):
        self.df = helper.read_djson()

    def get_list_by_city(self,city):
        dt = self.df[self.df['city'].isin(['Vaughan'])]
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


