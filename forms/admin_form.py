from forms.catalog_form import CatalogForm


class AdminForm:
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

    def verify_children_headers(self, selected_item):
        children = selected_item.find_elements_by_css_selector(self.elements.item_child)
        if len(children) > 0:
            for i in range(len(children)):
                children = self.browser.find_elements_by_css_selector(self.elements.item_child)
                child = children[i]
                child.click()
                header = self.browser.find_elements_by_css_selector(self.elements.header)
                assert len(header) > 0, "Заголовок не найден"

    def verify_menu_items_headers(self):
        app_menu = self.elements.app_menu
        item_list = app_menu.find_elements_by_css_selector(self.elements.menu_items)
        for i in range(len(item_list)):
            item_list = self.browser.find_elements_by_css_selector(self.elements.menu_items)
            item = item_list[i]
            item.click()
            selected_item = self.elements.selected_menu_item
            self.verify_children_headers(selected_item)
            header = self.browser.find_elements_by_css_selector(self.elements.header)
            assert len(header) > 0, "Заголовок не найден"

    def open_catalog(self):
        self.browser.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
        return CatalogForm(self.browser)


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

    @property
    def app_menu(self):
        return self.browser.find_element_by_css_selector("ul#box-apps-menu")

    @property
    def menu_items(self):
        css_selector = "li[id*='app-']"
        return css_selector

    @property
    def selected_menu_item(self):
        return self.browser.find_element_by_css_selector("li[id*='app'].selected")

    @property
    def item_child(self):
        css_selector = "li[id*='doc-']"
        return css_selector

    @property
    def header(self):
        css_selector = "td h1"
        return css_selector
