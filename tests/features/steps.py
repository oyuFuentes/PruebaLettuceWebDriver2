from lettuce import *

from lettuce_webdriver.util import AssertContextManager
import lettuce_webdriver.webdriver 
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys

@before.all
def setup_browser():
	world.browser = webdriver.Chrome()

@step('I go to "(.*?)"')
def i_go_to_url(step, url):
	world.response = world.browser.get(url)


def find_field_by_class(browser, attribute):
    xpath = "//input[@class='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False


@step('I fill in field with class "(.*?)" with "(.*?)"')
def fill_in_textfield_by_class(step, field_name, value):
    with AssertContextManager(step):
        text_field = find_field_by_class(world.browser, field_name)
        text_field.clear()
        text_field.send_keys(value, Keys.ENTER)
