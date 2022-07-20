import time
import datetime
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from PageObjects.Utils.TestData import TestData
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
action = ActionChains(driver)
options = Options()


def openBrowser():
    driver.maximize_window()
    driver.get(TestData.OFFICIAL_PAGE_LINK)
    allure.step("Opening the Browser")
    options.add_argument("--disable-notifications")


def closeBrowser():
    driver.quit()


def cssSelector(ByElement):
    css = (By.CSS_SELECTOR, ByElement)
    return css


def xpathLocator(ByElement):
    xpath = (By.XPATH, ByElement)
    return xpath


def tagName(ByElement):
    tag_Name = (By.TAG_NAME, ByElement)
    return tag_Name


def moveIntoView(webElement):
    action.move_to_element(webElement).perform()
    # driver.execute_script("arguments[0].scrollIntoView();", webElement)


def isElementPresent(webElement):
    presence = WebDriverWait(driver, 10).until(ec.visibility_of_element_located(webElement)).is_displayed()
    if not presence:
        allure.attach(driver.get_screenshot_as_png(), name='Failed Shot', attachement_type=AttachmentType.PNG)
    return presence


def clearTheInputField(byLocator):
    return WebDriverWait(driver, 10).until(ec.visibility_of_element_located(byLocator)).clear()


def enterTheInputValue(byLocator, addValue):
    return WebDriverWait(driver, 10).until(ec.visibility_of_element_located(byLocator)).send_keys(addValue)


def clickOnTheButton(buttonLocator):
    driver.implicitly_wait(5)
    return WebDriverWait(driver, 10).until(ec.visibility_of_element_located(buttonLocator)).click()


def waitForElementToBeVisibleAndClickable(buttonLocator):
    try:
        isElementPresent(buttonLocator)
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(buttonLocator)).click()
    except NoSuchElementException:
        print("No Such Element Exception.")


def switchToFrame(frameLocator):
    driver.switch_to.frame(frameLocator)


def switchToParentFrame():
    return driver.switch_to_default_content()


def useTabKeys():
    time.sleep(5)
    action.send_keys(Keys.TAB)


def useSpaceKeys():
    time.sleep(2)
    action.send_keys(Keys.SPACE)


def closeNewBrowserTab():
    time.sleep(5)
    driver.close()


def passPresentDate(dateLocator):
    now = datetime.datetime.now()
    today = now.strftime("%m-%d-%Y")
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(dateLocator)).send_keys(today)


def clickByUsingEnterKey(byLocator):
    return WebDriverWait(driver, 10).until(ec.visibility_of_all_elements_located(byLocator)).send_keys(Keys.ENTER)


def javaScriptExecutorClick(byLocator):
    driver.execute_script(byLocator)


def isElementEnable(webElement):
    presence = WebDriverWait(driver, 10).until(ec.visibility_of_element_located(webElement)).is_enabled()
    print(presence)
    if not presence:
        allure.attach('ScreenShot', driver.get_screenshot_as_png())
    return presence


def openBrowserToCheck(url):
    driver.get(url)
    allure.step("Opening the Browser")


def verifyForText(webElement):
    textPart = WebDriverWait(driver, 0).until(ec.visibility_of_element_located(webElement)).text
    print(textPart)
    return textPart


def moveToTheElement(byElement):
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(byElement))
    action.move_to_element_with_offset(WebDriverWait(driver, 10).until(ec.visibility_of_element_located(byElement)), 20,
                                       0).click().perform()


def closeBrowserNotification():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")


def switchWindow(window):
    driver.switch_to.window(driver.window_handles[window])


def openNewTab(new_url):
    # Open a new window
    driver.execute_script("window.open('');")

    # Switch to the new window and open new URL
    switchWindow(1)
    driver.get(new_url)


def refreshTab():
    driver.refresh()


def closeTab():
    driver.close()


def previousPage():
    driver.back()