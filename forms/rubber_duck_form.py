from model.rubber_duck import RubberDuck


class RubberDuckForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)

    def make_campaign_rubber_duck_obj(self):
        rubber_duck_name = self.elements.rubber_duck_name.text
        rubber_duck_price = self.elements.rubber_duck_price.text.split("$")[1]
        rubber_duck_discount_price = self.elements.rubber_duck_discount_price.text.split("$")[1]
        rubber_duck = RubberDuck(name=rubber_duck_name, price=int(rubber_duck_price),
                                 discount_price=int(rubber_duck_discount_price))
        return rubber_duck

    def verify_campaign_rubber_duck_name(self, expected_name):
        actual_rubber_duck = self.make_campaign_rubber_duck_obj()
        assert expected_name == actual_rubber_duck.name, "Название товара на странице товара отличается от ожидаемого"

    def verify_campaign_rubber_duck_price(self, expected_price):
        actual_rubber_duck = self.make_campaign_rubber_duck_obj()
        assert expected_price == actual_rubber_duck.price, "Цена товара на странице товара отличается от ожидаемой"

    def verify_campaign_rubber_duck_discount_price(self, expected_discount_price):
        actual_rubber_duck = self.make_campaign_rubber_duck_obj()
        assert expected_discount_price == actual_rubber_duck.discount_price, "Акционная цена товара на странице товара отличается от ожидаемой"

    def verify_campaign_rubber_duck_price_element_properties(self):
        regular_price = self.elements.rubber_duck_price
        assert "119, 119, 119" in regular_price.value_of_css_property('color')
        assert "line-through" in regular_price.value_of_css_property("text-decoration")

    def verify_campaign_rubber_duck_discount_price_element_properties(self):
        discount_price = self.elements.rubber_duck_discount_price
        assert "204, 0, 0" in discount_price.value_of_css_property('color')
        assert int(discount_price.value_of_css_property('font-weight')) > 400

    def compare_campaign_rubber_duck_price_elements(self):
        regular_price = self.elements.rubber_duck_price
        discount_price = self.elements.rubber_duck_discount_price
        regular_price_font_size = float(regular_price.value_of_css_property('font-size').split("px")[0])
        discount_price_font_size = int(discount_price.value_of_css_property('font-size').split("px")[0])
        assert regular_price_font_size < discount_price_font_size


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def rubber_duck_name(self):
        return self.browser.find_element_by_css_selector("h1[itemprop='name']")

    @property
    def rubber_duck_price(self):
        return self.browser.find_element_by_xpath("//*[@class='regular-price']")

    @property
    def rubber_duck_discount_price(self):
        return self.browser.find_element_by_xpath("//*[@class='campaign-price']")
