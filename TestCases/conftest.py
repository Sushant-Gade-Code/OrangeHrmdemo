import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def Setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Chrome Launching Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Firefox Launching Browser")
    elif browser == 'Edge':
        driver = webdriver.Edge()
        print("Edge Launching Browser")
    else:
        print("Headless")
        opt=webdriver.ChromeOptions()
        opt.add_argument("headless")
        driver=webdriver.Chrome(options=opt)
    driver.maximize_window()
    return driver


# @pytest.fixture(params=[
#     ("Admin","Admin123"),
#     ("Admin","Admin123"),
#     ("Admin","Admin123"),
#     ("Admin","Admin123"),
#                         ])
# def getDataforlogin(request):
#     return request.param


@pytest.fixture(params=[
    ("Admin", "admin123", "Pass"),
    ("Admin1", "admin123", "Fail"),
    ("Admin", "admin1231", "Fail"),
    ("Admin1", "admin1231", "Fail")
])
def getDataforlogin(request):
    return request.param