import time
import allure
from faker import Faker
import platform

from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from metaclasses.meta_locator import MetaLocator
from selenium.webdriver import Keys

faker = Faker()

class UIHelper(metaclass=MetaLocator):

    os_name = platform.system()
    CMD_CTRL = Keys.COMMAND if os_name == "darwin" else Keys.CONTROL

    def __init__(self, driver):
        """
        Инициализация класса UIHelper.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=1)
        self.actions = ActionChains(self.driver)
        self.fake = Faker()

    def find(self, locator: tuple, message: str = "", wait: bool = False) -> WebElement:
        """
        Находит элемент на странице, с ожиданием или без него.

        :param locator: Кортеж с локатором элемента.
        :param message: Сообщение об ошибке, если элемент не найден.
        :param wait: Использовать ожидание или сразу искать элемент.
        :return: WebElement — найденный элемент.
        """
        if wait:
            element = self.wait.until(EC.visibility_of_element_located(locator), message=message)
        else:
            element = self.driver.find_element(*locator)
        return element

    def find_all(self, locator: tuple, message: str = "", wait: bool = True) -> list[WebElement]:
        """
        Находит все элементы, соответствующие локатору.

        :param locator: Кортеж с локатором элементов.
        :param message: Сообщение об ошибке, если элементы не найдены.
        :param wait: Использовать ожидание или сразу искать элементы.
        :return: Список найденных WebElement.
        """
        if wait:
            elements = self.wait.until(EC.visibility_of_all_elements_located(locator), message=message)
        else:
            elements = self.driver.find_elements(*locator)
        return elements

    def fill(self, locator: tuple, text: str, clear: bool = True):
        """
        Заполняет поле ввода текстом.

        :param locator: Кортеж с локатором поля.
        :param text: Текст для ввода.
        :param clear: Очистить поле перед вводом (по умолчанию True).
        :return: None
        """
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def click(self, locator: tuple, message: str = ""):
        """
        Выполняет клик по элементу.

        :param locator: Локатор элемента (например, XPATH).
        :param message: Сообщение об ошибке при таймауте.
        :return: None
        """
        self.wait.until(EC.element_to_be_clickable(locator), message=message).click()

    def screenshot(self, name: str = faker.name()):
        """
        Делает скриншот текущего экрана и прикрепляет его к отчёту Allure.

        :param name: Имя скриншота.
        :return: None
        """
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def wait_for_invisibility(self, locator: WebElement, message: str = ""):
        """
        Ожидает, пока элемент станет невидимым.

        :param locator: Локатор элемента.
        :param message: Сообщение об ошибке при таймауте.
        :return: None
        """
        self.wait.until(EC.invisibility_of_element_located(locator), message=message)

    def wait_for_visibility(self, locator: WebElement, message: str = ""):
        """
        Ожидает, пока элемент станет видимым.

        :param locator: Локатор элемента.
        :param message: Сообщение об ошибке при таймауте.
        :return: None
        """
        self.wait.until(EC.visibility_of_element_located(locator), message=message)

    def wait_for_text_element(self, locator: WebElement, text: str, message: str = ""):
        """
        Ожидает появления указанного текста в элементе.

        :param locator: Локатор элемента.
        :param text: Текст, который ожидается в элементе.
        :param message: Сообщение об ошибке при таймауте.
        :return: None
        """
        self.wait.until(EC.text_to_be_present_in_element(locator, text), message=message)

    def wait_for_text_in_web_element(self, element, text: str, message: str = None):
        """
        Ожидает появления текста в веб-элементе.

        :param element: Веб-элемент, в котором нужно дождаться текста.
        :param text: Ожидаемый текст.
        :param message: Сообщение об ошибке при таймауте.
        :return: Элемент, если текст найден.
        """
        try:
            self.wait.until(lambda driver: text in element.text)
            return element
        except Exception as e:
            if message:
                raise TimeoutException(message)
            raise e

    def scroll_by(self, x, y):
        """
        Прокручивает страницу на указанное количество пикселей.

        :param x: Горизонтальное смещение.
        :param y: Вертикальное смещение.
        :return: None
        """
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        """
        Прокручивает страницу до самого низа.

        :return: None
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        """
        Прокручивает страницу к самому верху.

        :return: None
        """
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, locator):
        """
        Прокручивает страницу до указанного элемента.

        :param locator: Локатор элемента.
        :return: None
        """
        self.actions.scroll_to_element(self.find(locator))
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 500,
        });
        """)
