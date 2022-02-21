from forms.main_form import MainForm
from forms.rubber_duck_form import RubberDuckForm
from model.rubber_duck import RubberDuck


def test_verify_campaign_rubber_duck_name(browser):
    expected_rubber_duck = RubberDuck(name="Yellow Duck", price=20, discount_price=18)
    main_form = MainForm(browser)
    rubber_duck_form = RubberDuckForm(browser)
    main_form.open()
    main_form.verify_campaign_rubber_duck_name(expected_rubber_duck.name)
    main_form.open_campaign_rubber_duck_card()
    rubber_duck_form.verify_campaign_rubber_duck_name(expected_rubber_duck.name)


def test_verify_campaign_rubber_duck_prices(browser):
    expected_rubber_duck = RubberDuck(name="Yellow Duck", price=20, discount_price=18)
    main_form = MainForm(browser)
    rubber_duck_form = RubberDuckForm(browser)
    main_form.open()
    main_form.verify_campaign_rubber_duck_price(expected_rubber_duck.price)
    main_form.verify_campaign_rubber_duck_discount_price(expected_rubber_duck.discount_price)
    main_form.open_campaign_rubber_duck_card()
    rubber_duck_form.verify_campaign_rubber_duck_price(expected_rubber_duck.price)
    rubber_duck_form.verify_campaign_rubber_duck_discount_price(expected_rubber_duck.discount_price)


def test_verify_price_element_properties(browser):
    main_form = MainForm(browser)
    rubber_duck_form = RubberDuckForm(browser)
    main_form.open()
    main_form.verify_campaign_rubber_duck_price_element_properties()
    rubber_duck_form.verify_campaign_rubber_duck_price_element_properties()


def test_verify_discount_price_element_properties(browser):
    main_form = MainForm(browser)
    rubber_duck_form = RubberDuckForm(browser)
    main_form.open()
    main_form.verify_campaign_rubber_duck_discount_price_element_properties()
    rubber_duck_form.verify_campaign_rubber_duck_discount_price_element_properties()


def test_compare_price_elements(browser):
    main_form = MainForm(browser)
    rubber_duck_form = RubberDuckForm(browser)
    main_form.open()
    main_form.compare_campaign_rubber_duck_price_elements()
    rubber_duck_form.compare_campaign_rubber_duck_price_elements()
