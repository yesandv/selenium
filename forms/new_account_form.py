from selenium.webdriver.support.select import Select


class NewAccountForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)

    def open(self):
        self.browser.get("http://localhost/litecart/en/create_account")

    def create_account(self, account):
        first_name = self.elements.first_name
        first_name.send_keys(account.first_name)
        last_name = self.elements.last_name
        last_name.send_keys(account.last_name)
        address = self.elements.address
        address.send_keys(account.address)
        postcode = self.elements.postcode
        postcode.send_keys(account.postcode)
        city = self.elements.city
        city.send_keys(account.city)
        self.elements.country.click()
        self.elements.country_option(account.country).click()
        state = Select(self.elements.state)
        state.select_by_visible_text(account.state)
        email = self.elements.email
        email.send_keys(account.email.lower())
        phone = self.elements.phone
        phone.send_keys(account.phone)
        password = self.elements.password
        password.send_keys(account.password)
        confirm_password = self.elements.confirm_password
        confirm_password.send_keys(account.password)
        self.elements.create_account_btn.click()


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def first_name(self):
        return self.browser.find_element_by_css_selector("input[name='firstname']")

    @property
    def last_name(self):
        return self.browser.find_element_by_css_selector("input[name='lastname']")

    @property
    def address(self):
        return self.browser.find_element_by_css_selector("input[name='address1']")

    @property
    def postcode(self):
        return self.browser.find_element_by_css_selector("input[name='postcode']")

    @property
    def city(self):
        return self.browser.find_element_by_css_selector("input[name='city']")

    @property
    def country(self):
        return self.browser.find_element_by_css_selector("span .select2-selection")

    def country_option(self, country):
        return self.browser.find_element_by_xpath(f"//li[contains(@id, 'select2') and text()='{country}']")

    @property
    def state(self):
        return self.browser.find_element_by_css_selector("select[name='zone_code']")

    @property
    def email(self):
        return self.browser.find_element_by_css_selector("input[name='email']")

    @property
    def phone(self):
        return self.browser.find_element_by_css_selector("input[name='phone']")

    @property
    def password(self):
        return self.browser.find_element_by_css_selector("input[name='password']")

    @property
    def confirm_password(self):
        return self.browser.find_element_by_css_selector("input[name='confirmed_password']")

    @property
    def create_account_btn(self):
        return self.browser.find_element_by_css_selector("button[name='create_account']")
