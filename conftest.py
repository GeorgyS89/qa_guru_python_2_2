import pytest
from selene.support.shared import browser

@pytest.fixture()
def browser_size():
    browser.config.window_width, browser.config.window_height = 1920, 1080
    browser.open('https://google.com')
    yield