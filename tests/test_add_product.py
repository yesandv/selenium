from forms.admin_form import AdminForm
from model.rubber_duck import RubberDuck


def test_add_new_product(browser):
    new_duck = RubberDuck(name="Painter Rubber Duck", price=10)
    admin_form = AdminForm(browser)
    admin_form.sign_in(username="admin", password="admin", remember_me=True)
    catalog_form = admin_form.open_catalog()
    catalog_form.add_new_product(new_duck, status="Enabled")
    catalog_form.verify_product_has_been_added(new_duck)
