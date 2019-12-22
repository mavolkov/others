from selenium import webdriver  # для веб
import time

# ссылка:
link = "https://music.yandex.ru/users/extra.music.tri/playlists/3"

print('\nStarted.\n')

browser = webdriver.Chrome('/Users/misha/documents/megafon_numbers/chromedriver')  # драйвер браузера
# скачать драйвер: https://sites.google.com/a/chromium.org/chromedriver/home
browser.get(link)  # переходим на страницу и логинемся
time.sleep(15)
# browser.get(link)           # обновляем для страховки



browser.execute_script("window.scrollTo(0, 600);") # прокручиваем, чтобы песни были на всю страницу
try:
    elements = browser.find_elements_by_class_name(
        "d-icon_heart-full-colorless")  # сохр. все найденные сердечки в список
    counter = 0
    print(elements)
    for element in elements:  # идем по всем крестикам
        element.click()  # нажимаем на них
        #time.sleep(1) # задержка 1 сек на каждой песне
        counter += 1  # считаем нажатия
        if(counter % 12 == 0): # если удалили 12 песен, прокручиваем страницу ниже
            browser.execute_script("window.scrollBy(0, window.innerHeight);")
        

except Exception:
    print('№1. Какая-то ошибка...')
    time.sleep(1)
    browser.close()  # закрываем браузер
    print('Удалено песен: ', counter)
    print('\nFinished.\n')
else:
    print('№2. Всё хорошо. Исключения не было.')
    time.sleep(1)
    browser.close()  # закрываем браузер
    print('Удалено песен: ', counter)
    print('\nFinished.\n')


'''
#простой рабочий вариант, умер на 10 номере также из-за отсутствия прокрутки
while(True):
    browser.find_element_by_class_name("d-icon_heart-full-colorless").click()
'''

'''
# прокрутка по странично
for i in range(10):
    time.sleep(2)
    browser.execute_script("window.scrollBy(0, window.innerHeight);")
'''
