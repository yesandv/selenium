from model.geo_zone import GeoZone


class GeoZonesForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)

    def open(self):
        self.browser.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

    def verify_geo_zones_are_sorted_alphabetically(self):
        geo_zone_list = self.elements.get_geo_zone_list()
        for geo_zone in geo_zone_list:
            geo_zone.zone_list = self.elements.get_zone_list(geo_zone.id)
            sorted_zone_list = sorted(geo_zone.zone_list)
            assert geo_zone.zone_list == sorted_zone_list, f"Zones of {geo_zone.name} are not sorted alphabetically"


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def geo_zone_table(self):
        return self.browser.find_element_by_css_selector("table.dataTable")

    def get_geo_zone_list(self):
        geo_zones = []
        table = self.geo_zone_table
        rows = table.find_elements_by_css_selector("tr.row")
        for row in rows:
            attributes = row.find_elements_by_tag_name("td")
            geo_zone = GeoZone()
            geo_zone.id = attributes[1].text
            geo_zone.name = attributes[2].text
            geo_zones.append(geo_zone)
        return geo_zones

    @property
    def zone_table(self):
        return self.browser.find_element_by_class_name("dataTable")

    def get_zone_list(self, geo_zone_id):
        self.browser.get(f"http://localhost/litecart/admin/?app=geo_zones&doc=edit_geo_zone&page=1&geo_zone_id={geo_zone_id}")
        zone_list = []
        table = self.zone_table
        rows = table.find_elements_by_css_selector("tr")
        for row in rows[1:-1]:
            zone = row.find_element_by_xpath("./td[3]//option[@selected]").text
            zone_list.append(zone)
        return zone_list
