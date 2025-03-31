from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
import os


driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get(
    r"https://pipeline2.kindermorgan.com/Capacity/OpAvailPoint.aspx?code=NGPL")


datetoday = date.today()
Jan012025 = date.fromisoformat(r"2025-01-01")
deltaDay = timedelta(days=1)

curdate = Jan012025

while curdate <= datetoday:
    # datel.clear()
    sleep(5)
    datel = driver.find_element(
        By.CSS_SELECTOR, "input.bodytext.igte_NautilusEditInContainer")
    elem = driver.find_element(
        By.ID, 'WebSplitter1_tmpl1_ContentPlaceHolder1_HeaderBTN1_btnDownload')

    print("clicking the date changer")
    datel.click()
    print("breathing space")
    datel.send_keys(Keys.BACK_SPACE)
    datel.send_keys(Keys.BACK_SPACE)
    datel.send_keys(Keys.BACK_SPACE)
    datel.send_keys(Keys.BACK_SPACE)
    datel.send_keys(Keys.BACK_SPACE)
    datel.send_keys(Keys.BACK_SPACE)
    datel.send_keys(Keys.BACK_SPACE)
    datel.send_keys(Keys.BACK_SPACE)
    datel.send_keys(Keys.BACK_SPACE)
    datel.send_keys(Keys.BACK_SPACE)
    print(f"enternig {curdate.strftime(r"%m%d%Y")}")
    datel.send_keys(curdate.strftime(r"%m%d%Y"))

    datel.send_keys(Keys.RETURN)

    sleep(3)

    elem.click()
    print(f"download clicked for {curdate}")
    curdate += deltaDay
    sleep(5)
    print("refreshing the page")
    try:
        driver.refresh()
    except Exception as e:
        print(e)


print("quitting")
driver.quit()
