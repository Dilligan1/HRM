from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from helpers.ui_helper import UIHelper
from metaclasses.meta_locator import MetaLocator

class BasePage(metaclass=MetaLocator):

    _MESSAGE_NOTIFICATIONS = "//*[@class='ossn-notification-messages']//span[@class='ossn-notification-container']"
    _SENDER_NAME = "//div[@class='ossn-notification-messages']//a[@class='name']"

    def __init__(self, driver):
        self.driver = driver
        self.ui = UIHelper(self.driver)
        self.wait = WebDriverWait(self.driver, timeout=15, poll_frequency=1)


    allure.step("Open page")
    def open(self):
        self.driver.get(self._PAGE_URL)

    allure.step("Check page is opened")
    def is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_URL))

    allure.step("Check new messages exist and open it")
    def is_new_messages_exist(self):
        notification = self.ui.find(self._MESSAGE_NOTIFICATIONS, wait=True)
        if int(notification.text) != '0':
            self.driver.refresh()
            notification.click()
    allure.step("Check message author is {author_name}")
    def check_message_author(self, author_name):
        sender = self.ui.find(self._SENDER_NAME, wait=True)
        assert author_name in  sender.text, f"Expected author name '{author_name}', but got '{sender.text}'"



    def click_menu_item(self, menu_item_locator, submenu_item_locator):
        import time
        from selenium.common.exceptions import NoSuchElementException

        # Ждём, пока страница загрузится (проверяем, что URL изменился с login)
        time.sleep(1)
        
        try:
            # Проверяем, видно ли подменю сразу (меню уже раскрыто)
            submenu_item = self.ui.find(submenu_item_locator, wait=False)
            if submenu_item and submenu_item.is_displayed():
                submenu_item.click()
                return
        except NoSuchElementException:
            # Элемент не найден в DOM - кликаем по меню для раскрытия
            pass
        except Exception:
            # Элемент найден, но не виден - кликаем по меню для раскрытия
            pass

        # Кликаем по меню для раскрытия
        menu_item = self.ui.find(menu_item_locator, wait=True)
        menu_item.click()
        # Даём время на анимацию раскрытия меню
        time.sleep(0.5)

        # Ждём появления сабменю после клика и кликаем
        self.ui.find(submenu_item_locator, wait=True).click()

