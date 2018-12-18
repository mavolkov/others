from selenium import webdriver  # для веб
import time

# ссылка:
link = "https://vk.com/docs"

print('\nStarted.\n')

browser = webdriver.Chrome('/Users/misha/documents/megafon_numbers/chromedriver')  # драйвер браузера
# скачать драйвер: https://sites.google.com/a/chromium.org/chromedriver/home
browser.get(link)           # переходим на страницу и логинемся
time.sleep(15)
browser.get(link)           # обновляем для страховки

elements = browser.find_elements_by_class_name("docs_delete_row")  # сохр. все найденные крестики в список
counter = 0
for element in elements:    # идем по всем крестикам
    element.click()         # нажимаем на них
    counter += 1            # считаем нажатия
print('Удалено документов: ', counter)

time.sleep(5)
browser.close()     # закрываем браузер

print('\nFinished.\n')
