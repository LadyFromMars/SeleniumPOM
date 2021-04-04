from selenium import webdriver as wd
import unittest
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------------------Chrome-------------------------

def setUp(set_browser):
    global driver
    if set_browser == 'chrome':

        # Set Prefferences
        chromeOptions = wd.ChromeOptions()
        prefs = {"download.default_directory": "/Users/natallia/PycharmProjects/mod/tstlog"}
        chromeOptions.add_experimental_option("prefs", prefs)
        chromedriver = "/Users/natallia/pycharmProjects/mod/venv/drivers/chromedriver"

        driver = wd.Chrome(executable_path=chromedriver, options=chromeOptions)

    # ---------------------Firefox-------------------------
    elif set_browser == 'firefox':
        driver = wd.Firefox(executable_path='/Users/natallia/pycharmProjects/mod/venv/drivers/geckodriver')


    # ---------------------Browser not set-------------------------
    else:
        print('Browser is not set')

    return driver
