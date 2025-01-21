from playwright.sync_api import Page, Locator


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def main_link(self):
        return self.page.locator("div.tn-atom a[href='#main']").all()

    @property
    def about_link(self):
        return self.page.locator("a.tn-atom[href='#about']").all()

    @property
    def moreinfo_link(self):
        return self.page.locator("a.tn-atom[href='#moreinfo']").all()

    @property
    def cases_link(self):
        return self.page.locator("a.tn-atom[href='#cases']").all()

    @property
    def reviews_link(self):
        return self.page.locator("a.tn-atom[href='#Reviews']").all()

    @property
    def contacts_link(self):
        return self.page.locator("a.tn-atom[href='#contacts']").all()

    @property
    def specialists_link(self):
        return self.page.locator("a.tn-atom[href='#specialists']").all()

    def section_locators(self):
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
        self.page.goto("https://effective-mobile.ru")

    def go_to_section(self, section_locator: Locator):
        section_locator.click()
