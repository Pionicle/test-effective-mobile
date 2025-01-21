from playwright.sync_api import Page, Locator


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def main_link(self):
        """Локатор для главной раздела."""
        return self.page.locator("div.tn-atom a[href='#main']").all()

    @property
    def about_link(self):
        """Локатор для раздела 'О нас'."""
        return self.page.locator("a.tn-atom[href='#about']").all()

    @property
    def moreinfo_link(self):
        """Локатор для раздела 'Услуги'."""
        return self.page.locator("a.tn-atom[href='#moreinfo']").all()

    @property
    def cases_link(self):
        """Локатор для раздела 'Проекты'."""
        return self.page.locator("a.tn-atom[href='#cases']").all()

    @property
    def reviews_link(self):
        """Локатор для раздела 'Отзывы'."""
        return self.page.locator("a.tn-atom[href='#Reviews']").all()

    @property
    def contacts_link(self):
        """Локатор для раздела 'Контакты'."""
        return self.page.locator("a.tn-atom[href='#contacts']").all()

    @property
    def specialists_link(self):
        """Локатор для раздела 'Выбрать специалиста'."""
        return self.page.locator("a.tn-atom[href='#specialists']").all()

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
