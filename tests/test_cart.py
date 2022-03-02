from forms.cart_form import CartForm
from forms.main_form import MainForm
from forms.rubber_duck_form import RubberDuckForm


def test_add_to_cart(browser):
    main_form = MainForm(browser)
    cart_form = CartForm(browser)
    rubber_duck_form = RubberDuckForm(browser)
    main_form.open()
    for i in range(3):
        main_form.open_first_item()
        rubber_duck_form.add_to_cart(i)
        main_form.open()
    main_form.open_cart()
    cart_form.empty()
