from forms.sign_in_form import SignInForm
from forms.countries_form import CountriesForm


def test_countries_and_zones(browser):
    admin_form = SignInForm(browser)
    admin_form.sign_in(username="admin", password="admin", remember_me=True)
    countries_form = CountriesForm(browser)
    countries_form.open()
    countries_form.verify_countries_are_sorted_alphabetically()
    countries_form.verify_zones_are_sorted_alphabetically()
