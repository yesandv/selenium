from forms.admin_auth_form import AdminAuthForm


def test_sign_in_to_admin(browser):
    admin_form = AdminAuthForm(browser)
    admin_form.open()
    admin_form.log_in(username="admin", password="admin")


def test_sign_in_to_admin_with_remember_me_checkbox(browser):
    admin_form = AdminAuthForm(browser)
    admin_form.open()
    admin_form.select_remember_me_checkbox()
    admin_form.log_in(username="admin", password="admin")
