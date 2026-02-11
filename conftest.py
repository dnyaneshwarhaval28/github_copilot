import pytest
from playwright.sync_api import sync_playwright
from core.config_manager import ConfigManager


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment: dev/qa/prod")


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    cfg = ConfigManager.load_config(env)
    return cfg


@pytest.fixture(scope="session")
def browser(config):
    with sync_playwright() as p:
        browser_type = config["browser"]
        headless = config["headless"]

        browser = getattr(p, browser_type).launch(headless=headless)
        yield browser
        # browser.close()


@pytest.fixture(scope="function")
def page(browser, config):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(config["timeout"])
    yield page
    # page.close()


@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]


@pytest.fixture(scope="session")
def urls(config):
    return config["urls"]
