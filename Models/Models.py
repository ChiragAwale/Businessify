class Merchant:
    def __init__(self, name, category, geocode):
        self.name = name
        self.category = category
        self.lat = geocode["lat"]
        self.lng = geocode["lng"]

class User:
    def __init__(self,userId,firstName,lastName,email,phone):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone