from forms.main_form import MainForm
from forms.new_account_form import NewAccountForm
from model.account import Account


def test_sign_up_and_sign_in(browser):
    account = Account()
    new_account_form = NewAccountForm(browser)
    new_account_form.open()
    new_account_form.create_account(account)
    main_form = MainForm(browser)
    main_form.log_out()
    main_form.log_in(account.email, account.password)
    main_form.log_out()
