from forms.geo_zones_form import GeoZonesForm
from forms.sign_in_form import SignInForm


def test_geo_zones(browser):
    admin_form = SignInForm(browser)
    admin_form.sign_in(username="admin", password="admin", remember_me=True)
    geo_zones_form = GeoZonesForm(browser)
    geo_zones_form.open()
    geo_zones_form.verify_geo_zones_are_sorted_alphabetically()
