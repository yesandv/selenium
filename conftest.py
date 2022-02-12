import json

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser(config_as_json):
    if config_as_json.get("browser") == "Firefox":
        browser = webdriver.Firefox()
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
