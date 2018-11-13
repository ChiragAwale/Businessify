import requests
import serviceLayer.helper as helper
import Models.Models as models


API_CODE = "787add7451c5173af617ca2c5ce53497"
merchants = []

""" FOR ONLINE VERSION
def public_transit():
    requestUrl = 'http://api.reimaginebanking.com/merchants?key='+API_CODE
    print(requestUrl)
    resp = requests.get(requestUrl)
    helper.read_json(resp.content)
"""

#Populates a merchant list with merchant objects
def merchants_set():
    data = helper.read_json_from_file()
    for i in data:
        #print(i)
        #Filter data without geo code, and with geocode 0
        if "geocode" in i:
            if i["geocode"]["lat"] is not 0:
                current = models.Merchant(i["name"],i["category"],i["geocode"])
            merchants.append(current)


merchants_set()

"""
for merchant in merchants:
    print(merchant.category)
"""