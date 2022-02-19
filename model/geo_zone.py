class GeoZone:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        self.zone_list = []

    def __eq__(self, other):
        return self.zone_list == other.zone_list

    def __repr__(self):
        return f"Geo Zone: zone_list={', '.join(self.zone_list)}"
