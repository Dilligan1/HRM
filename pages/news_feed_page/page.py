import allure
from base.base_page import BasePage
from config.urls import Urls
from pages.news_feed_page.components.post_form import PostFormComponent
class NewsPage(BasePage):

    _PAGE_URL = Urls.NEWS_FEED_PAGE

    _POST_BLOCK = "//div[@class='post-contents']//p[1]"

    def __init__(self, driver):
        super().__init__(driver)
        self.post_form = PostFormComponent(driver)


    @allure.step("Is post published")
    def is_post_published(self, expected_text, visibility):
        post = self.ui.find(self._POST_BLOCK, wait=False)
        if visibility == "public":
            assert post.text == expected_text
        else:
            assert post.text != False