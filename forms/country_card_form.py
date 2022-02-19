from model.country import Zone


class CountryCardForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)

    def verify_zones_are_sorted_alphabetically(self):
        zone_list = self.elements.get_zone_list()
        zone_name_list = [zone.name for zone in zone_list]
        sorted_zone_name_list = sorted(zone_name_list)
        assert zone_name_list == sorted_zone_name_list, "Список зон не отсортирован в алфавитном порядке"


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def zone_table(self):
        return self.browser.find_element_by_class_name("dataTable")

    def get_zone_list(self):
        zone_list = []
        table = self.zone_table
        self.browser.execute_script("arguments[0].scrollIntoView();", table)
        rows = table.find_elements_by_css_selector("tr")
        for row in rows[1:-1]:
            attributes = row.find_elements_by_css_selector("td")
            zone = Zone()
            zone.id = attributes[0].text
            zone.code = attributes[1].text
            zone.name = attributes[2].text
            zone_list.append(zone)
        return zone_list
