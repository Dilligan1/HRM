import time

import allure

from base.base_page import BasePage


class PostFormComponent(BasePage):
    _POST_TEXTAREA = "//textarea[@name='post']"

    _TAG_FRIEND_BUTTON = "//li[contains(@class, 'tag-friend')]"
    _TAG_FRIEND_FIELD = "//input[@id='token-input-ossn-wall-friend-input']"

    _ADD_IMAGE_BUTTON = "//li[contains(@class, 'menu-photo')]"
    _UPLOAD_IMAGE_INPUT = "//input[@id='multipleupload-wall']"
    _PRIVACY_SETTINGS_BUTTON = "//div[@class='ossn-wall-privacy']"


    _SAVE_PRIVACY_SETTINGS_BUTTON = "//a[text()='Save']"
    _POST_BUTTON = "//input[@value='Post']"

    # Radios

    _RADIO_PRIVATE_PUBLIC_STATUS = "(//input[@class='ossn-radio-input'])[1]"
    _RADIO_PRIVATE_FRIENDS_STATUS= "(//input[@class='ossn-radio-input'])[2]"

    TAG_FRIEND_BY_NAME = lambda self, name: ("xpath", f"//div[@class='token-input-dropdown']//li//img[@title='{name}']")


    @allure.step("Write post_form")
    def write_post(self, text: str):
        self.ui.fill(self._POST_TEXTAREA, text)
        self.ui.screenshot()

    @allure.step("Tag friend")
    def tag_friends(self, friends: str | list):
        """
        This method tags friends
        :param friends: List full names
        :return:
        """
        if isinstance(friends, str):
            self.ui.click(self._TAG_FRIEND_BUTTON, "TAG FRIEND")
            self.ui.fill(self._TAG_FRIEND_FIELD, friends)
            locator = self.TAG_FRIEND_BY_NAME(friends)
            self.ui.find(locator, wait=True).click()
        elif isinstance(friends, list):
            for friend in friends:
                self.ui.click(self._TAG_FRIEND_BUTTON, "TAG FRIEND")
                self.ui.fill(self._TAG_FRIEND_FIELD, friend)
                locator = self.TAG_FRIEND_BY_NAME(friend)
                self.ui.find(locator, wait=True).click()

        else:
            raise Exception("Incorrect data")

    @allure.step("Choose post visibility status")
    def set_visibility_status(self, status: str):
        """
        This method accepts post status visibility status
        :param status: public/friends
        :return: None
        """
        # self.ui.find(self._PRIVACY_SETTINGS_BUTTON).click()
        # public_status = self.ui.find(self._RADIO_PRIVATE_PUBLIC_BUTTON).is_selected()
        # if public_status and status == "public":
        #     self.ui.click(self._SAVE_PRIVACY_SETTINGS_BUTTON, "Save button")
        # elif public_status and status == "friends":
        #     self.ui.click(self._RADIO_PRIVATE_FRIENDS_BUTTON)
        #     self.ui.click(self._SAVE_PRIVACY_SETTINGS_BUTTON, "Save button")
        self.ui.find(self._PRIVACY_SETTINGS_BUTTON, wait=True).click()

        if status == "public":
            self.ui.find(self._RADIO_PRIVATE_PUBLIC_STATUS, wait=True).click()
            radio_status = self.ui.find(self._RADIO_PRIVATE_PUBLIC_STATUS)
            if radio_status.is_selected():
                self.ui.click(self._SAVE_PRIVACY_SETTINGS_BUTTON, "Save button")

        elif status == "friends":
            self.ui.find(self._RADIO_PRIVATE_FRIENDS_STATUS, wait=True).click()
            radio_status = self.ui.find(self._RADIO_PRIVATE_FRIENDS_STATUS)
            if radio_status.is_selected():
                self.ui.click(self._SAVE_PRIVACY_SETTINGS_BUTTON, "Save button")







    @allure.step("Upload feed")
    def upload_image(self, source: str):
        self.ui.find(self._ADD_IMAGE_BUTTON, wait=True).click()
        self.ui.fill(self._UPLOAD_IMAGE_INPUT, source)
        self.ui.screenshot()

    @allure.step("Post")
    def publish(self):
        self.ui.find(self._POST_BUTTON, "Post button", wait=True).click()







