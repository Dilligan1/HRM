import time

from base.base_page import BasePage
import allure
from config.urls import Urls

class MessagesPage(BasePage):


    _PAGE_URL = Urls.MESSAGES_PAGE

    _MESSAGE_AREA = "//textarea[@name='message']"
    _SEND_BUTTON = "//input[@type='submit' and @value='Send']"
    _MESSAGE_ROWS = "//div[contains(@class, 'message-box-sent')]//span"


    @allure.step("Choose thread with {first_name} {last_name}")
    def choose_thread(self, first_name: str, last_name: str):
        locator = ("xpath", f"//div[@class='name' and text()='{first_name} {last_name}']")
        self.ui.click(locator)

    @allure.step("Send message")
    def send_message(self, message: str):
        self.ui.fill(self._MESSAGE_AREA, message)
        self.ui.click(self._SEND_BUTTON)

    @allure.step("Check last sent message")
    def is_message_sent(self, message):
        timeout = 10
        last_message = None


        all_message = self.ui.find_all(self._MESSAGE_ROWS)
        initial_count = len(all_message)


        while len(all_message) == initial_count:
            time.sleep(1)
            all_message = self.ui.find_all(self._MESSAGE_ROWS)
            timeout -= 1

            if timeout == 0:
                raise Exception("Message was not sent within the expected time.")

        last_message = all_message[-1]
        self.ui.wait_for_text_in_web_element(last_message, message)

        print(last_message.text)
