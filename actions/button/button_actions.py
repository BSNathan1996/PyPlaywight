from PyPlaywight.src.common.helper.helper import Helper
from PyPlaywight.src.pages.button.button import ButtonPage
from playwright.sync_api import Page

class Button_Actions:
    def __init__(self, page: Page, helper: Helper):
        self.page = page
        self.helper = helper
        
    def verify_gotohomeBtn(self):
        self.helper.click(ButtonPage.gotoHome_button)
        self.page.wait_for_url("https://www.qaplayground.com/", timeout=2000)

    def verify_disabledBtn(self):
        assert self.helper.is_visible(ButtonPage.disabled_button)
        assert self.helper.is_disabled(ButtonPage.disabled_button)

    def verify_doubleClickBtn(self):
        assert self.helper.is_visible(ButtonPage.double_click_button)
        self.page.locator(ButtonPage.double_click_button).dblclick()
        assert self.helper.is_visible(ButtonPage.result_notification)
        result_text = self.helper.get_text(ButtonPage.result_notification)

        assert result_text == "You Double-clicked on button!"

    def verify_rightClickBtn(self):
        assert self.helper.is_visible(ButtonPage.right_click_button)
        self.page.locator(ButtonPage.right_click_button).click(button="right")
        assert self.helper.is_visible(ButtonPage.result_notification)
        result_text = self.helper.get_text(ButtonPage.result_notification)

        assert result_text == "You Right-clicked on button!"



