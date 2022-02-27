import os
import time

from selenium.webdriver.support.select import Select


class NewProductForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)

    def fill_in_information(self, new_product, status):
        if status != "Disabled":
            self.elements.status(1).click()
        self.elements.name.send_keys(new_product.name)
        self.elements.code.send_keys(new_product.code)
        self.elements.categories(new_product.category).click()
        default_category = Select(self.elements.default_category)
        default_category.select_by_visible_text(new_product.category)
        self.elements.product_groups.click()
        self.elements.quantity.clear()
        self.elements.quantity.send_keys(1)
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, "painter_rubber_duck.jpeg")
        self.elements.upload_image.send_keys(file_path)
        self.elements.valid_from.send_keys(new_product.valid_from.strftime("%d-%m-%Y"))
        self.elements.valid_to.send_keys(new_product.valid_to.strftime("%d-%m-%Y"))
        self.elements.information_tab.click()
        manufacturer = Select(self.elements.manufacturer)
        manufacturer.select_by_visible_text(new_product.manufacturer)
        self.elements.keywords.send_keys("rubber duck")
        self.elements.short_description.send_keys(f"Short Description of the {new_product.name}")
        self.elements.description.send_keys(f"Full Description of the {new_product.name}")
        self.elements.head_title.send_keys(new_product.name)
        self.elements.meta_description.send_keys(new_product.name)
        self.elements.price_tab.click()
        self.elements.purchase_price.clear()
        self.elements.purchase_price.send_keys(new_product.price)
        currency = Select(self.elements.currency)
        currency.select_by_visible_text("Euros")
        self.elements.usd_price.send_keys(new_product.price + 2)
        self.elements.eur_price.send_keys(new_product.price)
        self.elements.save_btn.click()
        time.sleep(15)


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def general_tab(self):
        return self.browser.find_element_by_css_selector("div #tab-general")

    def status(self, value):
        return self.browser.find_element_by_xpath(f"//input[@name='status' and @value='{value}']")

    @property
    def name(self):
        return self.browser.find_element_by_css_selector("input[name='name[en]']")

    @property
    def code(self):
        return self.browser.find_element_by_css_selector("input[name='code']")

    def categories(self, value):
        return self.browser.find_element_by_xpath(f"//input[@name='categories[]' and @data-name='{value}']")

    @property
    def default_category(self):
        return self.browser.find_element_by_css_selector("select[name='default_category_id']")

    @property
    def product_groups(self):
        return self.browser.find_element_by_xpath("//input[@name='product_groups[]' and @value='1-3']")

    @property
    def quantity(self):
        return self.browser.find_element_by_css_selector("input[name='quantity']")

    @property
    def upload_image(self):
        return self.browser.find_element_by_css_selector("input[name='new_images[]']")

    @property
    def valid_from(self):
        return self.browser.find_element_by_css_selector("input[name='date_valid_from']")

    @property
    def valid_to(self):
        return self.browser.find_element_by_css_selector("input[name='date_valid_to']")

    @property
    def information_tab(self):
        return self.browser.find_element_by_css_selector("a[href='#tab-information']")

    @property
    def manufacturer(self):
        return self.browser.find_element_by_css_selector("select[name='manufacturer_id']")

    @property
    def keywords(self):
        return self.browser.find_element_by_css_selector("input[name='keywords']")

    @property
    def short_description(self):
        return self.browser.find_element_by_css_selector("input[name='short_description[en]']")

    @property
    def description(self):
        return self.browser.find_element_by_css_selector("[name='description[en]']")

    @property
    def head_title(self):
        return self.browser.find_element_by_css_selector("input[name='head_title[en]']")

    @property
    def meta_description(self):
        return self.browser.find_element_by_css_selector("input[name='meta_description[en]']")

    @property
    def price_tab(self):
        return self.browser.find_element_by_css_selector("a[href='#tab-prices']")

    @property
    def purchase_price(self):
        return self.browser.find_element_by_css_selector("input[name='purchase_price']")

    @property
    def currency(self):
        return self.browser.find_element_by_css_selector("select[name='purchase_price_currency_code']")

    @property
    def usd_price(self):
        return self.browser.find_element_by_css_selector("input[name='prices[USD]']")

    @property
    def eur_price(self):
        return self.browser.find_element_by_css_selector("input[name='prices[EUR]']")

    @property
    def save_btn(self):
        return self.browser.find_element_by_css_selector("button[name='save']")
