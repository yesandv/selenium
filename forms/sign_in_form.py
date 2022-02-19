from forms.admin_console_form import AdminConsoleForm


class SignInForm:
    def __init__(self, browser):
        self.browser = browser
        self.elements = Elements(browser)

    def open(self):
        self.browser.get("http://localhost/litecart/admin/")

    def log_in(self, username, password):
        self.elements.username.send_keys(username)
        self.elements.password.send_keys(password)
        self.elements.login_btn.click()

    def select_remember_me_checkbox(self):
        self.elements.remember_me_checkbox.click()

    def sign_in(self, username, password, remember_me=False):
        self.open()
        if remember_me:
            self.select_remember_me_checkbox()
        self.log_in(username, password)
        return AdminConsoleForm


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def username(self):
        return self.browser.find_element_by_name("username")

    @property
    def password(self):
        return self.browser.find_element_by_name("password")

    @property
    def remember_me_checkbox(self):
        return self.browser.find_element_by_name("remember_me")

    @property
    def login_btn(self):
        return self.browser.find_element_by_name("login")
