# coding=utf-8

from tests.pages.base import BasePage

from tests.elements.messages.send_panel import SendPanel
from tests.elements.messages.home_button import HomeButton
from tests.elements.messages.settings_button import SettingsButton
from tests.elements.messages.chat_header import ChatHeader
from tests.elements.messages.user_info import UserInfo
from tests.elements.messages.call import CallWindow
from tests.elements.messages.stickers import Stickers


class ChatPage(BasePage):
    def __init__(self, driver, id):
        self.url = 'http://ok.ru/messages/' + str(id)

        super(ChatPage, self).__init__(driver)

        self.send_panel = SendPanel(driver)
        self.home_button = HomeButton(driver)
        self.settings_button = SettingsButton(driver)
        self.chat_header = ChatHeader(driver)
        self.user_info = UserInfo(driver)
        self.call_window = CallWindow(driver)
        self.stickers = Stickers(driver)

    def message_input_text(self, text=None):
        if text is not None:
            self.send_panel.message_input().wait_for_presence().get().send_keys(text)

        return self.send_panel.message_input().wait_for_presence().get().get_attribute('innerHTML')

    def send_message(self):
        self.send_panel.send_button().wait_for_clickable().get().click()

    def get_message_input_placeholder(self):
        return self.send_panel.message_input().wait_for_visible().get().get_attribute('data-placeholder')

    def click_on_home_button(self):
        self.home_button.button().wait_for_clickable().get().click()

    def is_chat_closed(self):
        element = self.settings_button.button().wait_for_visible().get()
        return element is not None

    def is_call_window_opened(self):
        element = self.call_window.modal().wait_for_visible().get()
        return element is not None

    def is_calling(self):
        element = self.call_window.hang_up_button().wait_for_visible().get()
        return element is not None

    def click_on_chat_header(self):
        self.chat_header.head_name().wait_for_clickable().get().click()
        self.chat_header.head_name().wait_for_clickable().get().click()
        self.chat_header.head_name().wait_for_clickable().get().click()

    def click_on_call_button(self):
        self.chat_header.call_button().wait_for_clickable().get().click()
        self.chat_header.call_button().wait_for_clickable().get().click()
        self.chat_header.call_button().wait_for_clickable().get().click()
        self.chat_header.call_button().wait_for_clickable().get().click()
        self.chat_header.call_button().wait_for_clickable().get().click()
        self.chat_header.call_button().wait_for_clickable().get().click()

    def click_on_hang_up_button(self):
        self.call_window.hang_up_button().wait_for_clickable().get().click()

    def click_on_mic_button(self):
        self.call_window.mic_on_button().wait_for_clickable().get().click()

    def click_on_cam_button(self):
        self.call_window.cam_off_button().wait_for_clickable().get().click()

    def click_on_help_button(self):
        self.call_window.help_button().wait_for_clickable().get().click()

    def click_on_help_close_button(self):
        self.call_window.help_close_button().wait_for_clickable().get().click()

    def click_on_do_not_disturb_button(self):
        self.user_info.do_not_disturb_button().wait_for_clickable().get().click()

    def click_on_stickers_panel(self):
        self.send_panel.stickers_button().wait_for_clickable().get().click()
        self.send_panel.stickers_button().wait_for_clickable().get().click()
        self.send_panel.stickers_button().wait_for_clickable().get().click()
        self.send_panel.stickers_button().wait_for_clickable().get().click()

    def click_on_first_card(self):
        self.stickers.first_card().wait_for_clickable().get().click()

    def click_on_cards_tab(self):
        self.stickers.cards_tab_link().wait_for_clickable().get().click()

    def click_on_smiles_tab(self):
        self.stickers.smiles_tab_link().wait_for_clickable().get().click()

    def click_on_sad_smile(self):
        self.stickers.sad_smile().wait_for_clickable().get().click()

    def get_chat_header_name(self):
        return self.chat_header.head_name().wait_for_visible().get().get_attribute('innerHTML')

    def get_user_info_head_name(self):
        return self.user_info.head_name().wait_for_visible().get().get_attribute('innerHTML')
