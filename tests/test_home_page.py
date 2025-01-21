import pytest
import allure
from playwright.sync_api import Page
from pages.home_page import HomePage


@allure.feature("Навигация по секциям страницы")
@allure.title("Переход по якорной ссылке")
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
    """Тест для проверки локаторов секций на главной странице."""
    # Открываем главную страницу сайта
    with allure.step("Открываем главное окно сайта"):
        home_page = HomePage(page)
        home_page.open()

    # Получаем локаторы для указанной секции
    with allure.step(f"Получаем все локаторы для блока '{section}'"):
        locators = home_page.section_locators()[section]

    # Проходим по каждому локатору секции
    for index, locator in enumerate(locators):
        with allure.step(f"Локатор {index + 1}"):
            # Переходим по локатору
            with allure.step(f"Переходим по локатору"):
                home_page.go_to_section(locator)

            # Проверяем, что текущий URL соответствует ожидаемому
            with allure.step("Проверяем ссылки на соответствие"):
                assert home_page.url == f"https://effective-mobile.ru/{section}"
