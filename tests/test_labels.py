from forms.main_form import MainForm


def test_verify_rubber_ducks_have_label(browser):
    store = MainForm(browser)
    store.open()
    store.verify_rubber_ducks_have_label()
