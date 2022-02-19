class StoreMainForm:
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
            assert len(sticker) > 0, "У товара нет стикера"


class Elements:
    def __init__(self, browser):
        self.browser = browser

    @property
    def logo(self):
        css_selector = "img[src*='lonely-duck']"
        return css_selector

    @property
    def rubber_duck(self):
        css_selector = "li[class*='product']"
        return css_selector

    @property
    def sticker(self):
        css_selector = "div.sticker"
        return css_selector
