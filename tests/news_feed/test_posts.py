import os
import time
from faker import Faker
import allure
import pytest

from base.base_test import BaseTest
from fixtures.ui_fixtures import add_users

faker = Faker()

@allure.epic("News Feed")
@allure.feature("Posts")
class TestNewsFeed(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.parametrize("add_users", [1], indirect=True)
    @pytest.mark.parametrize("message, visibility",[
        ("Hello123", "public"),
        ("Hello", "friends")
    ])
    @allure.title("Create new post_form")
    def test_create_post_with_visibility(self, add_users, message, visibility):
        friend = add_users[0]

        self.login_page().open()
        self.login_page().login_as("admin")
        self.sidebar().links.open_news_feed()
        self.news_feed_page().post_form.write_post(message)
        self.news_feed_page().post_form.tag_friends('Keon Daniel')
        self.news_feed_page().post_form.upload_image(f'{os.getcwd()}/temp_file/img.png')
        self.news_feed_page().post_form.set_visibility_status(visibility)
        self.news_feed_page().post_form.publish()
        # Friends actions
        self.login_page(friend).open()
        self.login_page(friend).login_as("friend")
        self.sidebar(friend).links.open_news_feed()
        self.news_feed_page(friend).is_post_published(message, visibility)

    @pytest.mark.regress
    @allure.title("Create new busiiness page")
    def test_create_business_page(self,):
        self.login_page().open()
        self.login_page().login_as("admin")
        self.sidebar().business_page.create_new_business_page()
        self.new_business_page().fill_all_fields()
        self.new_business_page().is_page_created()
        time.sleep(5)

    @pytest.mark.regress
    @allure.title("Send a message to friend")
    @pytest.mark.parametrize("add_users", [1], indirect=True)
    def test_send_message_to_friend(self, add_users):
        admin = add_users[0]

        self.login_page().open()
        self.login_page().login_as("admin")
        self.sidebar().links.open_messages()
        self.messages_page().choose_thread("Megan", "Hanson")
        message = faker.word()
        self.messages_page().send_message(message)
        self.messages_page().is_message_sent(message)
        time.sleep(5)

        self.login_page(admin).open()
        self.login_page(admin).login_as("admin")
        self.news_feed_page(admin).is_new_messages_exist()
        self.news_feed_page(admin).check_message_author("Keon Daniel")
