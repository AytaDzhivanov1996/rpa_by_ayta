from engine import engine

from selenium.webdriver.common.by import By

import pandas
import time

def download_file(file_path):
    """Скачивание файла"""
    down_link = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'
    driver = engine(file_path)
    driver.get(down_link)
    time.sleep(3)

def rpa_challenge(file):
    """Выполнения скрипта для заполнения полей"""
    #Подготовка датафрейма
    data_frame = pandas.read_excel(file)
    data_frame.columns = ['First Name', 'Last Name', 'Company Name', 'Role in Company',
       'Address', 'Email', 'Phone Number']
    data_frame["Phone Number"] = data_frame["Phone Number"].astype(str)

    #Запуск Хрома, открытие страницы с испытанием, поиск кнопки Start
    driver = engine(file)
    driver.get("http://rpachallenge.com/")
    driver.maximize_window()
    driver.find_element(By.TAG_NAME, 'button').click()
    
    #Цикл для заполнения форм данными из датафрейма
    for person_index in range(len(data_frame)):
        cells = driver.find_elements(By.XPATH, '//form/div[@class="row"]/div')
 
        for i in range(len(cells)):
            person = data_frame.iloc[person_index]
            forms = cells[i].find_elements(By.XPATH, "//input")
            forms[i].send_keys(person[cells[i].text])
            time.sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, 'input.btn.uiColorButton').click()
    
    #Сохранение скриншота
    driver.save_screenshot('result.png')
    time.sleep(2)