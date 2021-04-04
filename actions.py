from selenium import webdriver as wd
import unittest
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import fn.xpathv as xp
import fn.log as lg
from selenium.common.exceptions import NoSuchElementException
import re


class actions(unittest.TestCase):


# ---------------------------------------------------
# Environment
# ---------------------------------------------------

    #-------------------------------
    #Browser settings

    global driver
    #driver = set.setUp('chrome')
    set_browser='chrome'


    #chrome
    if set_browser=='chrome':
        #Set Prefferences
        chromedriver = "/Users/natallia/pycharmProjects/mod/venv/drivers/chromedriver"
        driver = wd.Chrome(executable_path=chromedriver)
    #Firefox
    elif set_browser=='firefox':
        driver = wd.Firefox(executable_path='/Users/natallia/pycharmProjects/mod/venv/drivers/geckodriver')
    #Browser not set
    else:
        print ('Browser is not set')

    #-------------------------------
    #Make screenshot
    #Variables:
    #step_name (str) - name/description of the action performed
    #Example: fns.actions.take_screenshot('Add item to the cart')

    def take_screenshot(step_name):
        sh_path = "/Users/natallia/PycharmProjects/mod/tstlog/" #Save screenshots into directory
        step_name = re.sub(r'\W+', ' ', step_name)
        step_name=step_name.replace(" ", "_")
        save_sh_to=str(sh_path) + str(step_name) + ".png"
        driver.find_element_by_tag_name('body').screenshot(save_sh_to)


    #-------------------------------
    # Function to start test environment
    # Function used at the start of a test to pre-setup environment
    # Variables:
    # test_name - name of a test (name of a python file)
    # description - short description what test does
    #Example: fns.actions.start_test('cart01', 'Description: Search for item and add it to the cart. Verify price.')
    def start_test(test_name, description):
        print("---------------------------------------------------")
        print("Run started at: " + str(datetime.datetime.now()))
        print("Browser " + str(driver.name) + " " + str(driver.capabilities['browserVersion']))
        print("Test name: " + test_name)
        print(description)
        print("---------------------------------------------------")

        #Create html output file
        lg.log.create_html_output(test_name, description)
        # Get an URL
        driver.get('https://www.chewy.com/')
        # browser should be loaded in maximized window
        driver.maximize_window()
        # implicitly wait for page to load
        driver.implicitly_wait(2)


    #-------------------------------
    # Finish the test
    def tearDown():
        # close the browser
        driver.quit()

        print("---------------------------------------------------")
        print("Test Enviroment Shut Down")
        print("Run Complete at: " + str(datetime.datetime.now()))
        print("---------------------------------------------------")



# ------------------------------------------------
# Main actions
# ------------------------------------------------

    #-------------------------------
    # Single click (click on element)
    # Variables:
    # xpathkey (str)- xpath 'name' (key) from common file xpathv.py ('' if fullxpath used);
    # fullxpath (str)- xpath to locate the item ('' if xpathkey used);
    # step_name (str) - name/description of the action performed
    # screenshot (str) - 'y' if screen shot should be taken
    def click(xpathkey, fullxpath, step_name, screenshot):
        try:
            xpathv_f = xp.copmplete_xpath(xpathkey, fullxpath)
            #WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpathv_f)))
            driver.find_element_by_xpath(xpathv_f).click()
            #Create output
            lg.log.add_step(step_name, screenshot)
        except NoSuchElementException:
            print ("Element not found and test failed")
            driver.quit()



    #-------------------------------
    # Paste text into text/input field
    # Variables:
    # xpathkey (str)- xpath 'name' (key) from common file xpathv.py ('' if fullxpath used);
    # fullxpath (str)- xpath to locate the item ('' if xpathkey used);
    # clear (str) - 'y' if text/input field need to be cleared prior to pasting new text
    # text (str) - text to type into text/input field
    # step_name (str) - name/description of the action performed
    # Example: fns.actions.input("username", "", 'y', 'admin@gmail.com', 'Paste an email')

    def input(xpathkey, fullxpath, clear, text, step_name):
        try:
            xpathv_f = xp.copmplete_xpath(xpathkey, fullxpath)
            element = driver.find_element_by_xpath(xpathv_f)
            if clear == 'y':
                element.clear()
            else:
                pass
            element.send_keys(text)

            #Create output
            lg.log.add_step(step_name, 'y')

        except NoSuchElementException:
            print ("Element not found and test failed")
            print ('Step: ' + step_name)
            driver.quit()
# -------------------------------------------------
# Validation
# -------------------------------------------------

    #-------------------------------
    # Verify text value
    # Use: Get the text value from element and compare with expected value
    # Variables:
    # xpathkey (str)- xpath 'name' (key) from common file xpathv.py ('' if fullxpath used);
    # fullxpath (str)- xpath to locate the item ('' if xpathkey used);
    # expected_text (str) - expected text value
    # step_name (str) - name/description of the action performed

    def verify_text(xpathkey, fullxpath, expected_text, step_name):
        global status
        xpathv_f = xp.copmplete_xpath(xpathkey, fullxpath)
        # wait for element to appear
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpathv_f)))
        # Get text value
        textv = driver.find_element_by_xpath(xpathv_f).text
        textv = textv.strip()
        # Compare actual and expected values
        #tc = unittest.TestCase('__init__')
        #tc.assertEqual(text,textv)
        if expected_text == textv:
            print("Checkpoint passed: " + str(textv))
            status= 'pass'
            pass
        else:
            print("Checkpoint failed. Actual: " + str(textv) + " Expected: " + str(expected_text))
            status= 'fail'
        #Create output
        lg.log.add_step_checkpoint(step_name, status, expected_text, textv, 'n')
