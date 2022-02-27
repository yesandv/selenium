from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from forms.new_product_form import NewProductForm


class CatalogForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)

    def add_new_product(self, new_product, status="Disabled"):
        self.elements.add_new_product_btn.click()
        new_product_form = NewProductForm(self.browser)
        new_product_form.fill_in_information(new_product, status=status)

    def verify_product_has_been_added(self, new_product):
        WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Catalog')]")))
        assert len(self.elements.get_product(new_product.name)) == 1, "Товара нет в каталоге"


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def add_new_product_btn(self):
        return self.browser.find_element_by_css_selector("[href*='edit_product']")

    def get_product(self, product_name):
        return self.browser.find_elements_by_xpath(f"//a[text()='{product_name}']")
