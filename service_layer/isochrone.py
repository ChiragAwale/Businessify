import config_k as config
import requests

lat = "-118.22258"
lng = "33.99038"


def get_isochrone_mapbox(lat,lng,mode=None):
    request_url = "https://api.mapbox.com/isochrone/v1/mapbox/" +\
                 "driving/" +\
                 lat +\
                 "," +\
                 lng +\
                 "?contours_minutes=5,10,15" \
                 "&contours_colors=6706ce,04e813,4286f4" \
                 "&polygons=true" \
                 "&access_token="+config.MAPBOX_ACCESS_TOKEN
    #print(request_url)
    resp = requests.get(request_url)
    json_object = resp.json()
    #print(json_object["features"][0]["geometry"]["coordinates"])
    return json_object["features"][2]["geometry"]["coordinates"]


def get_isochrone_os(lat,lng,mode=None):
    request_url = "https://api.openrouteservice.org/isochrones?" \
                  "api_key=5b3ce3597851110001cf62482d5dd8411707474f89a029c4002c6d9a" \
                  "&locations=-77.0369,38.9072" \
                  "&profile=driving-car" \
                  "&range=60,120,600" \
                  "&smoothing=1"
    #print(request_url)
    resp = requests.get(request_url)
    json_object = resp.json()
    print(json_object["features"][0]["geometry"]["coordinates"])
    return json_object["features"][2]["geometry"]["coordinates"]


