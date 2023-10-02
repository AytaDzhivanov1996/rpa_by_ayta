from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def engine(file_path):
    """Функция создания движка для скачивания файла и открытия браузера"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
          "download.default_directory": file_path,
          "download.prompt_for_download": False,
          "download.directory_upgrade": True,
        })
    
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    return driver