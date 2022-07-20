from PageObjects.Utils.CommonMethods import *

EMAIL = cssSelector('#EmailInput')
PASSWORD = cssSelector('[id="inputPassword1"]')
SUBMIT_BUTTON = cssSelector('button[type="submit"]')
NEW_ALERT_POP_UP_CLOSE_BUTTON = cssSelector('i.src-styles-_iconFonts_icon.src-styles-_iconFonts_icon_cross_narrow_big.src-components-Popups-_styles_icon')


def setUserEmail(email):
    if isElementPresent(EMAIL):
        clearTheInputField(EMAIL)
        enterTheInputValue(EMAIL, email)
    else:
        raise Exception(str(EMAIL) + "is not present on Screen.")


def setUserPassword(password):
    if isElementPresent(PASSWORD):
        clearTheInputField(PASSWORD)
        enterTheInputValue(PASSWORD, password)
    else:
        raise Exception(str(PASSWORD) + "is not found on Screen.")


def clickOnSubmitButton():
    if isElementPresent(SUBMIT_BUTTON):
        clickOnTheButton(SUBMIT_BUTTON)
    else:
        raise Exception(str(SUBMIT_BUTTON) + "is not found on the Screen.")


def closeAnonymousPopUp():
    try:
        if isElementPresent(NEW_ALERT_POP_UP_CLOSE_BUTTON):
            clickOnTheButton(NEW_ALERT_POP_UP_CLOSE_BUTTON)
        else:
            raise Exception(str(NEW_ALERT_POP_UP_CLOSE_BUTTON), "is not present")

    except NameError:
        pass

