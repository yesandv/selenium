class AdminForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)

    def open(self):
        self.browser.get("http://localhost/litecart/admin/")
        return AdminForm

    def log_in(self, username, password):
        self.elements.username.send_keys(username)
        self.elements.password.send_keys(password)
        self.elements.login_btn.click()


class Elements:
    def __init__(self, browser):
        self.driver = browser

    @property
    def username(self):
        return self.driver.find_element_by_name("username")

    @property
    def password(self):
        return self.driver.find_element_by_name("password")

    @property
    def remember_me_checkbox(self):
        return self.driver.find_element_by_name("remember_me")

    @property
    def login_btn(self):
        return self.driver.find_element_by_name("login")
