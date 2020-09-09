from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)
    option1 = browser.find_element_by_css_selector("[name='text']")
    option1.send_keys(y)
    option2 = browser.find_element_by_class_name("btn.btn-primary")
    option2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
#element.send_keys(file_path)