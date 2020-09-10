import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                 help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    yield browser
    browser = webdriver.Chrome(options=options)
    print("\nquit browser..")
    browser.quit()