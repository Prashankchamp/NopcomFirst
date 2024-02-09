import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Test run in chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Test run in firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Test run in edge browser")
        driver = webdriver.Edge()
    else:
        print("Test run in headless browser")
        driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    yield driver
    driver.quit()
