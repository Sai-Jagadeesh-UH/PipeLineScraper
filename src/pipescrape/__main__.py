from .argParser import parser
from .argValidator import argValidator
from .logger import logging
from .exceptor import Custom_Error
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta, datetime
import sys


def log(msg: str):
    print(msg)
    logging.info(msg)


args = parser.parse_args()

if (x := argValidator(args).getString()):
    log(x)
else:
    try:
        from_date = date.today()
        till_date = date.today()

        if (args.on):
            from_date = datetime.strptime(args.on, r"%m%d%Y").date()
            till_date = datetime.strptime(args.on, r"%m%d%Y").date()
        elif (args.fro or args.till):
            from_date = datetime.strptime(args.fro, r"%m%d%Y").date()
            till_date = datetime.strptime(args.till, r"%m%d%Y").date()

        log(f"executing from {from_date} to {till_date}")

        driver = webdriver.Chrome()

        driver.implicitly_wait(5)

        driver.get(
            r"https://pipeline2.kindermorgan.com/Capacity/OpAvailPoint.aspx?code=NGPL")

        deltaDay = timedelta(days=1)
        curdate = from_date

        while curdate <= till_date:

            sleep(5)
            datel = driver.find_element(
                By.CSS_SELECTOR, "input.bodytext.igte_NautilusEditInContainer")
            elem = driver.find_element(
                By.ID, 'WebSplitter1_tmpl1_ContentPlaceHolder1_HeaderBTN1_btnDownload')

            # print("clicking the date changer")
            datel.click()
            # print("breathing space")
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
            log(f"entering {curdate.strftime(r'%m%d%Y')}")
            datel.send_keys(curdate.strftime(r"%m%d%Y"))

            datel.send_keys(Keys.RETURN)

            sleep(3)

            elem.click()
            log(f"download clicked for {curdate}")
            curdate += deltaDay
            sleep(5)
            log("refreshing the page")
            try:
                driver.refresh()
            except Exception as e:
                log("errored at refreshing the browser")
                raise Custom_Error(e, sys)

        log("quitting the browser")
        driver.quit()
    except Exception as e:
        raise Custom_Error(e, sys)
