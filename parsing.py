from selenium import webdriver  # для веб

# 1-я часть ссылки:
link_part1='https://moscow.shop.megafon.ru/connect/chnumber/fullnumber.html?page='
# 2-я часть ссылки:
link_part2='&search=1&onegroup=1&number_types_filter%5B7987%5D%5B0%5D=7991&search_area=metall'
number_of_links = 572           # количетсво веб-страниц с номерами

print('\nStarted.\n')

f_out = open('out.txt', 'w')            # файл для вывода номеров
browser = webdriver.Chrome('/Users/misha/Desktop/megafon_numbers/chromedriver')  # драйвер браузера
# скачать драйвер:
# https://sites.google.com/a/chromium.org/chromedriver/home
# сайт:
# https://moscow.shop.megafon.ru/connect/chnumber/fullnumber.html?page=1&search=1&onegroup=1&number_types_filter%5B7987%5D%5B0%5D=7991&search_area=metall

numbers_counter = 0
for i in range(1,number_of_links+1):        # идем по всем страницам
    #f_out.write('Page:'+str(i)+'\n')        # пишем номер страницы в файл
    browser.get(link_part1 + str(i) + link_part2)  # переходим на страницу
    elements = browser.find_elements_by_class_name("g_numbers_number")  # сохр. все классы с номерами в список
    for element in elements:                # идем по всем классам с номерами
        if element.text:                    # если не пусто
            f_out.write(element.text+'\n')  # записываем номер в файл
            numbers_counter += 1            # увеличиваем счетчик номеров
    print('Пройдена страница ', str(i))

browser.close()     # закрываем браузер
f_out.close()       # закрываем файл

print('Сохранено номеров:' + str(numbers_counter))
print('\nFinished.\n')