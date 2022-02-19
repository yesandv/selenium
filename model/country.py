class Country:
    def __init__(self, id=None, code=None, name=None, zones=None):
        self.id = id
        self.code = code
        self.name = name
        self.zones = zones

    def __eq__(self, other):
        return self.name == other.name and self.zones == other.zones

    def __repr__(self):
        return f"\nCountry: id='{self.id}', code='{self.code}', name='{self.name}', zones={self.zones}"


class Zone(Country):
    def __init__(self, id=None, code=None, name=None):
        Country.__init__(self, id, code, name)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return f"\nZone name='{self.name}'"
