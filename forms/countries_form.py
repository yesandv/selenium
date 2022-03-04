from forms.country_card_form import CountryCardForm
from model.country import Country


class CountriesForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)
        self.country_card_form = CountryCardForm(browser)

    def open(self):
        self.browser.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    def verify_countries_are_sorted_alphabetically(self):
        country_list = self.elements.get_country_list()
        country_name_list = [country.name for country in country_list]
        sorted_country_name_list = sorted(country_name_list)
        assert country_name_list == sorted_country_name_list, "Список стран не отсортирован в алфавитном порядке"

    def verify_zones_are_sorted_alphabetically(self):
        country_list = self.elements.get_country_list()
        for country in country_list:
            if country.zones > 0:
                self.browser.get(f"http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code={country.code}")
                self.country_card_form.verify_zones_are_sorted_alphabetically()

    def add_new_country(self):
        self.elements.add_new_country_btn.click()
        return CountryCardForm


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def country_table(self):
        return self.browser.find_element_by_css_selector("table.dataTable")

    def get_country_list(self):
        country_list = []
        table = self.country_table
        rows = table.find_elements_by_css_selector("tr.row")
        for row in rows:
            attributes = row.find_elements_by_tag_name("td")
            country = Country()
            country.id = attributes[2].text
            country.code = attributes[3].text
            country.name = attributes[4].text
            country.zones = int(attributes[5].text)
            country_list.append(country)
        return country_list

    @property
    def add_new_country_btn(self):
        return self.browser.find_element_by_css_selector(".button[href*='edit_country']")