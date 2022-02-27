from forms.admin_form import AdminForm


def test_verify_admin_menu_items(browser):
    admin_form = AdminForm(browser)
    admin_form.sign_in(username="admin", password="admin", remember_me=True)
    admin_form.verify_menu_items_headers()
