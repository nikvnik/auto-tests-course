from selenium import webdriver
import os 
import time
try:
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys("y1")
    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys("x1")
    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("email")
    image = browser.find_element_by_css_selector("[type='file']")
    image.send_keys(file_path)
    button = browser.find_element_by_css_selector("[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
#element.send_keys(file_path)