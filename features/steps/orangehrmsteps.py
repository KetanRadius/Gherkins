from behave import *
from selenium import webdriver


@given('launch firefox browser')
def launchbrowser(context):
    context.driver = webdriver.Firefox(
        executable_path="D:\Python_notebook\Drivers\geckodriver.exe")


@when('open orange hrm page')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath(
        "//*[@id='divLogo']/img").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
