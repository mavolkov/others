import time  # для задержки
from selenium import webdriver  # для веб
from selenium.common.exceptions import NoSuchElementException  # для исключения "не существует"

print('\nStarted\n')
links = []                  # список для ссылок
f_in = open('in.txt', 'r')  # файл со ссылками
for line in f_in:           # добавляем ссылки из файла в список
    links.append(line.strip())
f_in.close()                # закрываем файл

done_number = 0             # счетчик выполненных
fail_number = 0             # счетчик ошибок
link_number = 0             # счетчик пройденных ссылок
driver = webdriver.Chrome('/Users/misha/Desktop/extract/chromedriver')  # переменная браузера
for link in links:          # идем по всем ссылкам
    driver.get(link)        # открываем страницу
    try:
        element = driver.find_element_by_name('send')  # ищем элемент по имени
    except NoSuchElementException:  # если кнопки "скачать нет"
        link_number += 1    # +1 ссылка
        fail_number += 1    # +1 ошибка
        print("пусто   по ссылке №", link_number)
        time.sleep(2)       # ждем 2 сек.
    else:                   # если не было исключения
        element.click()     # нажимаем
        link_number += 1    # +1 ссылка
        done_number += 1    # +1 выполненная
        print('скачено по ссылке №', link_number)
        time.sleep(3)       # ждем 3 сек.

print('Done : ', done_number)
print('Fail : ', fail_number)
print('Total: ', link_number)
 
print('\nFinished\n')
# time.sleep(18000)  # пауза на 5 часов
# driver.close()  # закрываем браузер
