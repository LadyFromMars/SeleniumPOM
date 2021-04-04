import unittest
import fn.actions as fns
from fn.actions import *

class cmn(unittest.TestCase):

#---------------------------------------------------
# Environment
#---------------------------------------------------

#Function to start test enviroment

    def login(username, password):
        if username=='':
            username='example031@gmail.com'

        if password=='':
            password='testpass'

        #Click on account button
        fns.actions.click("account", "", "Click on account button", 'n')

        #Click Sign In button
        fns.actions.click("sign_in_by_text", "", 'Click Sign In button', 'n')

        #Paste email and password
        fns.actions.input("username", "", 'y', username, 'Paste an email')
        fns.actions.input("password", "", '', password, 'Paste a password')

        #Click Sign In button
        fns.actions.click('sign_in', '', 'Click Sign In button', 'y')
