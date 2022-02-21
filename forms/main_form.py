from forms.rubber_duck_form import RubberDuckForm
from model.rubber_duck import RubberDuck


class MainForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)

    def open(self):
        self.browser.get("http://localhost/litecart/en/")

    def verify_rubber_ducks_have_label(self):
        rubber_duck_list = self.browser.find_elements_by_css_selector(self.elements.rubber_duck)
        for i in range(len(rubber_duck_list)):
            rubber_duck = rubber_duck_list[i]
            sticker = rubber_duck.find_elements_by_css_selector(self.elements.sticker)
            assert len(sticker) > 0, "У товара нет стикера"

    def verify_campaign_rubber_duck_name(self, expected_name):
        actual_rubber_duck = self.elements.make_campaign_rubber_duck_obj(self.elements.campaign_duck)
        assert expected_name == actual_rubber_duck.name, "Название товара на главной странице отличается от ожидаемого"

    def open_campaign_rubber_duck_card(self):
        self.elements.campaign_duck.click()
        return RubberDuckForm

    def verify_campaign_rubber_duck_price(self, expected_price):
        actual_rubber_duck = self.elements.make_campaign_rubber_duck_obj(self.elements.campaign_duck)
        assert expected_price == actual_rubber_duck.price, "Цена товара на главной странице отличается от ожидаемой"

    def verify_campaign_rubber_duck_discount_price(self, expected_discount_price):
        actual_rubber_duck = self.elements.make_campaign_rubber_duck_obj(self.elements.campaign_duck)
        assert expected_discount_price == actual_rubber_duck.discount_price, "Акционная цена товара на главной странице отличается от ожидаемой"

    def verify_campaign_rubber_duck_price_element_properties(self):
        regular_price = self.elements.campaign_duck.find_element_by_xpath(".//*[@class='regular-price']")
        assert "119, 119, 119" in regular_price.value_of_css_property('color')
        assert "line-through" in regular_price.value_of_css_property("text-decoration")

    def verify_campaign_rubber_duck_discount_price_element_properties(self):
        discount_price = self.elements.campaign_duck.find_element_by_xpath(".//*[@class='campaign-price']")
        assert "204, 0, 0" in discount_price.value_of_css_property('color')
        assert int(discount_price.value_of_css_property('font-weight')) > 400

    def compare_campaign_rubber_duck_price_elements(self):
        regular_price = self.elements.campaign_duck.find_element_by_xpath(".//*[@class='regular-price']")
        discount_price = self.elements.campaign_duck.find_element_by_xpath(".//*[@class='campaign-price']")
        regular_price_font_size = float(regular_price.value_of_css_property('font-size').split("px")[0])
        discount_price_font_size = int(discount_price.value_of_css_property('font-size').split("px")[0])
        assert regular_price_font_size < discount_price_font_size


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def logo(self):
        css_selector = "img[src*='lonely-duck']"
        return css_selector

    @property
    def rubber_duck(self):
        css_selector = "li[class*='product']"
        return css_selector

    @property
    def sticker(self):
        css_selector = "div.sticker"
        return css_selector

    @property
    def campaign_duck(self):
        return self.browser.find_element_by_css_selector("#box-campaigns li")

    def make_campaign_rubber_duck_obj(self, campaign_duck):
        self.browser.execute_script("arguments[0].scrollIntoView();", campaign_duck)
        rubber_duck_name = campaign_duck.find_element_by_css_selector("div.name").text
        rubber_duck_price = campaign_duck.find_element_by_xpath(".//*[@class='regular-price']").text.split("$")[1]
        rubber_duck_discount_price = campaign_duck.find_element_by_xpath(".//*[@class='campaign-price']").text.split("$")[1]
        rubber_duck = RubberDuck(name=rubber_duck_name, price=int(rubber_duck_price), discount_price=int(rubber_duck_discount_price))
        return rubber_duck
