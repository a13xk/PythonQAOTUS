import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption(name="--browser")
    headless = request.config.getoption(name="--headless")

    if browser_name.lower() == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if headless:
            firefox_options.add_argument("--headless")

        browser = webdriver.Firefox(options=firefox_options)
    elif browser_name.lower() == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")

        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True

        browser = webdriver.Chrome(
            options=chrome_options,
            desired_capabilities=capabilities
        )
    else:
        raise NameError("Please specify correct browser name to initialize web driver.\n"
                        "Example: `pytest --browser=Chrome` or `pytest --browser=Firefox`")
    yield browser
    browser.quit()
#


@pytest.fixture(scope="function")
def opencart_base_url(request):
    return request.config.getoption("--opencart_url")
#


# Init hook
def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="Web driver for specified browser (defaults to firefox)"
    )

    parser.addoption(
        "--opencart_url",
        action="store",
        default="https://localhost",
        help="OpenCart base URL for tests (defaults to https://localhost)"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode (by default browser starts with GUI)"
    )
#
