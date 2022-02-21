from forms.sign_in_form import SignInForm


def test_sign_in_to_admin(browser):
    sign_in_form = SignInForm(browser)
    sign_in_form.open()
    sign_in_form.log_in(username="admin", password="admin")


def test_sign_in_to_admin_with_remember_me_checkbox(browser):
    sign_in_form = SignInForm(browser)
    sign_in_form.open()
    sign_in_form.select_remember_me_checkbox()
    sign_in_form.log_in(username="admin", password="admin")
