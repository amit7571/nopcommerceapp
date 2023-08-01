import pytest
from selenium import webdriver
import pytest_metadata

#Below is the code to take browser parameter from terminal and return the driver of that browser, that driver is used in test case file.
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        #specify default browser, it will run in this browser if no brower argument is provided in comment line.
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser): #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the Browser value to setup method
    return request.config.getoption("--browser")

#below is the comment we need to run in terminal to run tests parallel, where n specify the number of parallel running test.
# pytest -s -v -n=2 testCases/test_login.py --browser chrome

######## PyTest HTML Report#######
#It is hook for adding Environment info to HTML Report


def pytest_configure(config):
  metadata = config.pluginmanager.getplugin("metadata")
  print(metadata)
  if metadata:

      from pytest_metadata.plugin import metadata_key
      config.stash[metadata_key]['foo'] = 'bar'


#it is a hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Java_Home",None)
    metadata.pop("plugins",None)