import json

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FFOptions


@pytest.fixture(scope="session")
def browser(config_as_json):
    if config_as_json.get("browser") == "Firefox":
        browser = webdriver.Firefox()
    elif config_as_json.get("browser") == "Nightly":
        options = FFOptions()
        options.binary_location = '/Applications/Firefox Nightly.app/Contents/MacOS/firefox-bin'
        browser = webdriver.Firefox(firefox_options=options, executable_path='/usr/local/bin/geckodriver')
    elif config_as_json.get("browser") == "Safari":
        browser = webdriver.Safari()
    else:
        browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def config_as_json():
    with open("config.json") as config_as_json:
        config = json.load(config_as_json)
        return config
