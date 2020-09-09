from selenium import webdriver
import time
import math
#browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    y_button = browser.find_element_by_id("answer")
    y_button.send_keys(y)
    option1 = browser.find_element_by_class_name("form-check-input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    option2 = browser.find_element_by_css_selector("[value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
#browser.execute_script("window.scrollBy(0, 100);") #скролл на 100 пикселей
