from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

        # Метод принимает кейворд аргументы (kwargs)

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Добавляем аргумент nth со значением по умолчанию 0
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator).nth(nth)  # self.page.locator(locator)

    def click(self, nth: int = 0, **kwargs):
        # Добавили аргумент nth и передаем его в get_locator
        locator = self.get_locator(nth, **kwargs)
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        # Добавили аргумент nth и передаем его в get_locator
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        # Добавили аргумент nth и передаем его в get_locator
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)
