from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)

    def empty(self):
        for i in range(len(self.elements.order_items)):
            order = self.elements.order_items
            self.elements.remove_btn.click()
            wait = WebDriverWait(self.browser, 3)
            wait.until(EC.staleness_of(order[0]))


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def order_items(self):
        return self.browser.find_elements_by_css_selector("table.dataTable td.item")

    @property
    def remove_btn(self):
        return self.browser.find_element_by_css_selector("button[name='remove_cart_item']")
