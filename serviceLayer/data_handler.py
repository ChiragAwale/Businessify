import serviceLayer.helper as helper


class DataHandler:

    def __init__(self):
        self.df = helper.read_djson()

    def get_list_by_city(self,city):
        dt = self.df[self.df['city'].isin(['Vaughan'])]
        data = []
        for i in dt.index:
            data.append(dt.loc[i].to_json())

        print(data[1])
        return data
