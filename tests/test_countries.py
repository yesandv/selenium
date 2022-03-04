from forms.country_card_form import CountryCardForm
from forms.sign_in_form import SignInForm
from forms.countries_form import CountriesForm


def test_countries_and_zones(browser):
    admin_form = SignInForm(browser)
    admin_form.sign_in(username="admin", password="admin", remember_me=True)
    countries_form = CountriesForm(browser)
    countries_form.open()
    countries_form.verify_countries_are_sorted_alphabetically()
    countries_form.verify_zones_are_sorted_alphabetically()


def test_new_tab(browser):
    admin_form = SignInForm(browser)
    admin_form.sign_in(username="admin", password="admin", remember_me=True)
    countries_form = CountriesForm(browser)
    countries_form.open()
    countries_form.add_new_country()
    country_card = CountryCardForm(browser)
    country_card.open_links_in_new_tab()
