from base_components.sidebar.sidebar import Sidebar
from pages.login_page.page import LoginPage
from pages.news_businnes_page.page import CreateNewBusinessPage
from pages.news_feed_page.page import NewsPage
from pages.messages_page.page import MessagesPage



class BaseTest:

    def setup_method(self):
        #Pages
        self.login_page = lambda  driver = self.driver: LoginPage(driver)
        self.news_feed_page = lambda  driver = self.driver: NewsPage(driver)
        self.new_business_page = lambda  driver = self.driver: CreateNewBusinessPage(driver)
        self.messages_page = lambda  driver = self.driver: MessagesPage(driver)

        #Components
        self.sidebar = lambda  driver = self.driver: Sidebar(driver)
