from forms.admin_form import AdminForm


def test_log_in_to_admin(browser):
    admin_form = AdminForm(browser)
    admin_form.open()
    admin_form.log_in(username="admin", password="password")
