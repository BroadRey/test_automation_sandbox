import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def open_browser():
    browser.open('https://google.com')
    browser.config.window_width = 1366
    browser.config.window_height = 784


def test_query_with_nonexistent_text_should_find_nothing(open_browser):
    browser.element('[name="q"]').should(be.blank).type('dsjkfadjhfdjafhdjafdsh').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу dsjkfadjhfdjafhdjafdsh ничего не найдено. '))


def test_google_search(open_browser):
    browser.element('#APjFqb').should(be.blank).type('yashaka/selen').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
