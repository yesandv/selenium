from forms.admin_auth_form import AdminAuthForm
from forms.admin_console_form import AdminConsoleForm


def test_verify_admin_menu_items(browser):
    admin_auth_form = AdminAuthForm(browser)
    admin_console = AdminConsoleForm(browser)
    admin_auth_form.sign_in(username="admin", password="admin", remember_me=True)
    admin_console.verify_menu_items_headers()
