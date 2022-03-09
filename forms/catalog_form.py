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

    def open_category(self):
        self.browser.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")

    def open_products(self):
        products = self.elements.products
        for i in range(len(products)):
            products = self.elements.products
            product = products[i]
            product.click()
            for log in self.browser.get_log("browser"):
                print(log)
            self.browser.back()


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def add_new_product_btn(self):
        return self.browser.find_element_by_css_selector("[href*='edit_product']")

    def get_product(self, product_name):
        return self.browser.find_elements_by_xpath(f"//a[text()='{product_name}']")

    @property
    def products(self):
        return self.browser.find_elements_by_xpath("//tr[@class='row']//a[contains(@href, 'edit_product') and not (contains(@title, 'Edit'))]")