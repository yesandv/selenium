from forms.cart_form import CartForm
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
            assert len(sticker) == 1, "У товара не один стикер"

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
        grey_colour = regular_price.value_of_css_property('color').split("(")[1].split(")")[0].split(", ")
        assert len(set(grey_colour)) == 1
        assert "line-through" in regular_price.value_of_css_property("text-decoration")

    def verify_campaign_rubber_duck_discount_price_element_properties(self):
        discount_price = self.elements.campaign_duck.find_element_by_xpath(".//*[@class='campaign-price']")
        red_colour = discount_price.value_of_css_property('color').split("(")[1].split(")")[0].split(", ")
        assert red_colour[1] == red_colour[2]
        assert int(discount_price.value_of_css_property("font-weight")) > 400

    def compare_campaign_rubber_duck_price_elements(self):
        regular_price = self.elements.campaign_duck.find_element_by_xpath(".//*[@class='regular-price']")
        discount_price = self.elements.campaign_duck.find_element_by_xpath(".//*[@class='campaign-price']")
        regular_price_font_size = float(regular_price.value_of_css_property("font-size").split("px")[0])
        discount_price_font_size = int(discount_price.value_of_css_property("font-size").split("px")[0])
        assert regular_price_font_size < discount_price_font_size

    def log_in(self, email, password):
        self.elements.email.send_keys(email.lower())
        self.elements.password.send_keys(password)
        self.elements.log_in_btn.click()

    def log_out(self):
        self.elements.log_out.click()

    def open_first_item(self):
        self.elements.get_item(1).click()
        return RubberDuckForm

    def open_cart(self):
        self.elements.cart.click()
        return CartForm


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def rubber_duck(self):
        css_selector = ".product"
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

    @property
    def email(self):
        return self.browser.find_element_by_css_selector("input[name='email']")

    @property
    def password(self):
        return self.browser.find_element_by_css_selector("input[name='password']")

    @property
    def log_in_btn(self):
        return self.browser.find_element_by_css_selector("button[name='login']")

    @property
    def log_out(self):
        return self.browser.find_element_by_xpath("//div[@id='box-account']//a[text()='Logout']")

    def get_item(self, item_number):
        return self.browser.find_element_by_xpath(f"//ul[contains(@class, 'listing')]/li[{item_number}]")

    @property
    def cart(self):
        return self.browser.find_element_by_css_selector("a.content[href*='checkout']")
