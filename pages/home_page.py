from playwright.sync_api import Page, Locator


class HomePageLocators:
    """Класс для хранения локаторов."""

    MAIN_LINK = "div.tn-atom a[href='#main']"
    ABOUT_LINK = "a.tn-atom[href='#about']"
    MOREINFO_LINK = "a.tn-atom[href='#moreinfo']"
    CASES_LINK = "a.tn-atom[href='#cases']"
    REVIEWS_LINK = "a.tn-atom[href='#Reviews']"
    CONTACTS_LINK = "a.tn-atom[href='#contacts']"
    SPECIALISTS_LINK = "a.tn-atom[href='#specialists']"


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def main_link(self):
        """Локатор для главной раздела."""
        return self.page.locator(HomePageLocators.MAIN_LINK).all()

    @property
    def about_link(self):
        """Локатор для раздела 'О нас'."""
        return self.page.locator(HomePageLocators.ABOUT_LINK).all()

    @property
    def moreinfo_link(self):
        """Локатор для раздела 'Услуги'."""
        return self.page.locator(HomePageLocators.MOREINFO_LINK).all()

    @property
    def cases_link(self):
        """Локатор для раздела 'Проекты'."""
        return self.page.locator(HomePageLocators.CASES_LINK).all()

    @property
    def reviews_link(self):
        """Локатор для раздела 'Отзывы'."""
        return self.page.locator(HomePageLocators.REVIEWS_LINK).all()

    @property
    def contacts_link(self):
        """Локатор для раздела 'Контакты'."""
        return self.page.locator(HomePageLocators.CONTACTS_LINK).all()

    @property
    def specialists_link(self):
        """Локатор для раздела 'Выбрать специалиста'."""
        return self.page.locator(HomePageLocators.SPECIALISTS_LINK).all()

    @property
    def url(self) -> str:
        """Возвращает текущий URL страницы."""
        return self.page.url

    def section_locators(self):
        """Возвращает словарь локаторов для различных секций."""
        return {
            "#main": self.main_link,
            "#about": self.about_link,
            "#moreinfo": self.moreinfo_link,
            "#cases": self.cases_link,
            "#Reviews": self.reviews_link,
            "#contacts": self.contacts_link,
            "#specialists": self.specialists_link,
        }

    def open(self):
        """Открывает главную страницу."""
        self.page.goto("https://effective-mobile.ru")

    def go_to_section(self, section_locator: Locator):
        """Переходит к указанной секции."""
        section_locator.click()
