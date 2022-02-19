class AdminForm:
    def __init__(self, browser):
        self.driver = browser
        self.elements = Elements(browser)

    def verify_children_headers(self, selected_item):
        children = selected_item.find_elements_by_css_selector(self.elements.item_child)
        if len(children) > 0:
            for i in range(len(children)):
                children = self.driver.find_elements_by_css_selector(self.elements.item_child)
                child = children[i]
                child.click()
                header = self.driver.find_elements_by_css_selector(self.elements.header)
                assert len(header) > 0, "Заголовок не найден"

    def verify_menu_items_headers(self):
        app_menu = self.elements.app_menu
        item_list = app_menu.find_elements_by_css_selector(self.elements.menu_items)
        for i in range(len(item_list)):
            item_list = self.driver.find_elements_by_css_selector(self.elements.menu_items)
            item = item_list[i]
            item.click()
            selected_item = self.elements.selected_menu_item
            self.verify_children_headers(selected_item)
            header = self.driver.find_elements_by_css_selector(self.elements.header)
            assert len(header) > 0, "Заголовок не найден"


class Elements:
    def __init__(self, browser):
        self.browser = browser

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
