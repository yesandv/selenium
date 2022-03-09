from forms.admin_form import AdminForm


def test_get_logs(browser):
    admin_form = AdminForm(browser)
    admin_form.sign_in(username="admin", password="admin", remember_me=True)
    catalog_form = admin_form.open_catalog()
    catalog_form.open_category()
    catalog_form.open_products()
