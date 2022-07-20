import pytest
from PageObjects.Pages.Otp import *

from PageObjects.Pages.LogInPage import *
from PageObjects.Utils.TestData import TestData


def test_Existing_User_Login_Logout():
    openBrowser()
    setUserEmail(EMAIL)
    setUserPassword(PASSWORD)
    clickOnSubmitButton()
    closeAnonymousPopUp()
    closeBrowser()

