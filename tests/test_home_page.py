import pytest
import allure
from playwright.sync_api import Page
from pages.home_page import HomePage


@allure.feature("Навигация по секциям страницы")
@allure.description("Тест проверяет переход по секциям, используя якорные ссылки.")
@pytest.mark.parametrize(
    "section",
    [
        ("#main"),
        ("#about"),
        ("#moreinfo"),
        ("#cases"),
        ("#Reviews"),
        ("#contacts"),
        ("#specialists"),
    ],
)
def test_section_locators(page: Page, section: str):
    with allure.step("Открываем главное окно сайта"):
        home_page = HomePage(page)
        home_page.open()

    with allure.step(f"Получаем все локаторы для блока '{section}'"):
        locators = home_page.section_locators()[section]

    for index, locator in enumerate(locators):
        with allure.step(f"Локатор {index + 1}"):
            with allure.step(f"Переходим по локатору"):
                home_page.go_to_section(locator)

            with allure.step("Проверяем ссылки на соответствие"):
                expected_link = "https://effective-mobile.ru" + "/" + section
                assert home_page.page.url == expected_link
