import os
import time
import logging
from services import download_file, rpa_challenge

#Логирование
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

#Пользователь вводит папку, в которую хочет скачать файл
file_path = input("В какую папку скачать файл?")

#Скачивание файла
download_file(file_path)

#Скрипт для заполнения форм
rpa_challenge(f'{file_path}/challenge.xlsx')

if __name__ == '__main__':
    print('Задание выполнено успешно')
