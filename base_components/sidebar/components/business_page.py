import allure

from base.base_page import BasePage



class BusinessPage(BasePage):

    # Main link for click

    _BUSINESS_PAGE_LOCATOR = "//a[text()='Business Page']"

    # Business items
    _CREATE_NEW_PAGE_LOCATOR = "//li[text()='Create new page']"

    @allure.step("Open 'Create new page'")
    def create_new_business_page(self):
        self.click_menu_item(self._BUSINESS_PAGE_LOCATOR, self._CREATE_NEW_PAGE_LOCATOR)



