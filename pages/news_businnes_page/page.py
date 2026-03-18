import allure

from base.base_page import BasePage
from pages.news_businnes_page.components.page_builder import BusinessPageBuilder
from config.urls import Urls


class CreateNewBusinessPage(BasePage):

    _PAGE_URL = Urls.CREATE_NEW_BUSINESS_PAGE
    _BUSINESS_PAGE_COVER = "//div[@class='business-page-cover']"


    def __init__(self, driver):
        super().__init__(driver)
        self.page_builder = BusinessPageBuilder(driver)

    @allure.step("Open Create New Business Page")
    def is_page_created(self):
        self.ui.wait_for_visibility(self._BUSINESS_PAGE_COVER)


    def fill_all_fields(self):
        BusinessPageBuilder(self.driver).set_page_name("Test page") \
        .set_page_description("Test description") \
        .set_page_phone("122332344") \
        .set_page_address("Test Address") \
        .set_page_website("https://vk.com") \
        .build()

    def fill_required(self):
        BusinessPageBuilder(self.driver).set_page_name("Test page") \
        .set_page_description("Test description") \
        .set_page_phone("122332344") \
        .build()




