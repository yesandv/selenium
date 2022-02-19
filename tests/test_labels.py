from forms.store_main_form import StoreMainForm


def test_verify_rubber_ducks_have_label(browser):
    store = StoreMainForm(browser)
    store.open()
    store.verify_rubber_ducks_have_label()
