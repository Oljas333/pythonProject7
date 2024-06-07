from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

try:
    driver = webdriver.Firefox()
    driver.get("https://dev.mycar.kz/online-dealer")
    option1 = WebDriverWait(driver, 10)
    bth_element = driver.find_element(By.XPATH, "//img[@alt='Chery']")
    driver.execute_script("arguments[0].scrollIntoView(true);", bth_element)
    driver.execute_script("arguments[0].click();", bth_element)
    img_element = driver.find_element(By.XPATH, '//a[img[@alt="фото Chery Tiggo 7 Новая за 11190000 тенге"]]')
    driver.execute_script("arguments[0].scrollIntoView(true);", img_element)
    driver.execute_script("arguments[0].click();", img_element)
    txt_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text() ='В кредит']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", txt_element)
    bg_element = driver.find_element(By.XPATH, "//button[text() ='рассчитать в кредит']")
    driver.execute_script("arguments[0].click();", bg_element)
    h5_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()=48]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", h5_element)
    driver.execute_script("arguments[0].click();", h5_element)
    bg1_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Узнать решение']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", bg1_element)
    bg1_element.click()
    driver.find_element(By.XPATH, "//input[@aria-label='Имя*']").send_keys("Test")
    driver.find_element(By.XPATH, "//input[@aria-label='Номер телефона*']").send_keys(77776666666)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Далее']").click()
    bg1_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[4]/input"))
    )
    driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[4]/input").send_keys(0)
    driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[3]/input").send_keys(0)
    driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/input").send_keys(0)
    driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/input").send_keys(0)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='отменить предыдущую заявку']").click()
    bg4_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Заполнить анкету']"))
    )
    driver.execute_script("arguments[0].click();", bg4_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@aria-label='ИИН']").send_keys(801223300825)
    driver.find_element(By.XPATH, "//button[text()='далее']").click()
    bg4_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Женат/Замужем']"))
    )
    driver.execute_script("arguments[0].click();", bg4_element)
    driver.find_element(By.XPATH, "//button[text()='далее']").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div[3]/div/div[1]/div[1]/button").click()
    driver.find_element(By.XPATH, "//input[@aria-label='Поиск']").send_keys('Mycar')
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p[text()='Mycar Almaty, автосалон']"))
    ).click()
    driver.find_element(By.XPATH, "//input[@aria-label='Должность']").send_keys('Test')
    driver.find_element(By.XPATH, "//input[@aria-label='Номер телефона компании']").send_keys(77777777777)
    driver.find_element(By.XPATH, "//input[@aria-label='Лет']").send_keys(13)
    driver.find_element(By.XPATH, "//p[text()='Общий стаж работы']/following-sibling::node()[1]/descendant::input").send_keys(13)
    driver.find_element(By.XPATH, "//button[text()='далее']").click()
    driver.find_element(By.XPATH, "//input[@aria-label='Основной доход, ₸']").send_keys(1000000)
    driver.find_element(By.XPATH, "//button[text()='далее']").click()
    driver.find_element(By.XPATH, "//input[@aria-label='Номер телефона']").send_keys(77775555555)
    driver.find_element(By.XPATH, "//input[@aria-label='Имя и фамилия']").send_keys("Тест тест")
    driver.find_element(By.ID, "headlessui-menu-button-5").click()
    driver.find_element(By.ID, "headlessui-menu-item-9").click()
    driver.find_element(By.XPATH, "//button[text()='далее']").click()
    bth_element = driver.find_element(By.XPATH, "//button[text()='Отправить']")
    driver.execute_script("arguments[0].scrollIntoView(true);", bth_element)
    driver.execute_script("arguments[0].click();", bth_element)
    driver.save_screenshot("a.png")

finally:
    time.sleep(5)
    driver.quit()

