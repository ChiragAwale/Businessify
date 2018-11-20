import serviceLayer.helper as helper
import json

class DataHandler:

    def __init__(self):
        self.df = helper.read_djson()

    def get_list_by_city(self,city):
        dt = self.df[self.df['city'].isin(['Vaughan'])]
        d = dt.to_dict(orient='records')
        j = json.dumps(d)
        return j
