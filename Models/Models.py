class Merchant:
    def __init__(self, name, category, geocode):
        self.name = name
        self.category = category
        self.lat = geocode["lat"]
        self.lng = geocode["lng"]