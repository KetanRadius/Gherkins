from behave import *
from selenium import webdriver


@given('I launch firefox browser')
def launchbrowser(context):
    context.driver = webdriver.Firefox(
        executable_path="D:\Python_notebook\Drivers\geckodriver.exe")


@when('I open orange HRM Homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def enterUsername(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('Click on login button')
def login(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User must successfully login to the Dashboard page')
def closeBrowser(context):
    try:
        text = context.driver.find_element_by_xpath(
            "//*[@id='content']/div/div[1]/h1").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
