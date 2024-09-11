import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Укажите абсолютный путь к вашему веб-драйверу
driver_path = r'WebDriver/ChromeDriver/chromedriver.exe'

# Настройка опций для Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Включение headless режима
chrome_options.add_argument("--disable-gpu")  # Отключение GPU (необязательно, но рекомендуется)
chrome_options.add_argument("--window-size=1920x1080")  # Установка размера окна (необязательно, но может быть полезно)

# Создайте экземпляр веб-драйвера
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Откройте веб-сайт
driver.get('https://www.saucedemo.com/')

def find_and_send_keys(by, value, keys):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by, value))
    )
    element.send_keys(keys)

def find_and_click(by, value):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((by, value))
    )
    element.click()

# Авторизация
find_and_send_keys(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input', 'standard_user')
find_and_send_keys(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input', 'secret_sauce')
find_and_click(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/input')

# Добавляем товар в корзину
find_and_click(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')

# Находим корзину
find_and_click(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a')

# Находим кнопку CheckOut
find_and_click(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/button[2]')

# Заполнение формы
find_and_send_keys(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input', 'Ivan')
find_and_send_keys(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input', 'Ivanov')
find_and_send_keys(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input', '42123423')
find_and_click(By.XPATH, '/html/body/div/div/div/div[2]/div/form/div[2]/input')

# Завершение заказа
find_and_click(By.XPATH, '/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]')

# Проверка успешного заказа
title = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/span'))
).text
completeheader = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/h2').text
completetext = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div').text

if (title == 'Checkout: Complete!' and completeheader == 'Thank you for your order!'
        and completetext == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'):
    print('Товар был успешно заказан')
else:
    print('При заказе товара возникла ошибка')

# Закрытие браузера
driver.quit()
