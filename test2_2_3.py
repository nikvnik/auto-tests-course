from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_id("num1")
    num1 = num1.text
    num2 = browser.find_element_by_id("num2")
    num2 = num2.text
    sum_12 = int(num1)+int(num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum_12))
    option3 = browser.find_element_by_class_name("btn.btn-default")
    option3.click()
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()