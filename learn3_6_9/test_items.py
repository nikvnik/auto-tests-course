
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_language_link_and_find_button(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    assert browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"), "Is not button"