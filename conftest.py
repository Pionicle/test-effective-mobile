from playwright.sync_api import Playwright, sync_playwright, Browser
import pytest


@pytest.fixture(scope="session")
def browser():
    """Фикстура для запуска браузера перед тестом и его закрытия после."""
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser):
    """Фикстура для открытия новой страницы перед каждым тестом"""
    page = browser.new_page()
    yield page
    page.close()
