# -*- coding: utf-8 -*-

from base import BaseTest

from tests.pages.messages.chat import ChatPage


class MessagesTest(BaseTest):
    DEFAULT_USER_ID = 589325597219
    DEFAULT_MESSAGE_TEXT = 'test from selenium'

    MESSAGE_TEXT_INPUT_PLACEHOLDER = unicode('Напишите сообщение', 'utf-8')

    def test_message_send(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        self.assertEqual(chat_page.get_message_input_placeholder(), self.MESSAGE_TEXT_INPUT_PLACEHOLDER)

        chat_page.message_input_text(self.DEFAULT_MESSAGE_TEXT)
        chat_page.send_message()

        self.assertEqual(len(chat_page.message_input_text()), 1, 'message input has cleared')

    def test_home_button(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_home_button()

        self.assertTrue(chat_page.is_chat_closed(), 'chat has closed')

    def test_user_info_appearance(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        user_name = chat_page.get_chat_header_name()

        chat_page.click_on_chat_header()

        self.assertEqual(chat_page.get_chat_header_name(), user_name, 'chat header name has not boon changed')
        self.assertEqual(chat_page.get_user_info_head_name(), user_name, 'user info header name fills properly')

    def test_call(self):
        chat_page = ChatPage(self.driver, self.DEFAULT_USER_ID)
        chat_page.navigate()

        chat_page.click_on_call_button()

        self.assertTrue(chat_page.is_call_window_opened(), 'call window has been opened')
        self.assertTrue(chat_page.is_calling(), 'calling')

        chat_page.click_on_hang_up_button()

        self.assertTrue(chat_page.is_hanged_up(), 'hanged up')
