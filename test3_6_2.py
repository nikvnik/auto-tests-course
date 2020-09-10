import pytest
from selenium import webdriver
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('numbers', ["895","896","897","898","899","903","904","905"])
def test_guest_should_see_login_link(browser, numbers):
    browser.implicitly_wait(10)
    link = f"https://stepik.org/lesson/236{numbers}/step/1"
    browser.get(link)
    test1 = browser.find_element_by_tag_name("textarea")
    test1.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    text_element = browser.find_element_by_class_name("smart-hints__hint")
    text_text = text_element.text
    assert text_text == "Correct!", text_text
