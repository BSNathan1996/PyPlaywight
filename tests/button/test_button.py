from PyPlaywight.src.common.base.base import BasePage
import pytest
from PyPlaywight.actions.button.button_actions import Button_Actions
from tests.testData.button_data import ButtonData

@pytest.fixture
def button_actions(page, helper):
    base_actions = BasePage(page, helper)
    base_actions.goto_base()
    base_actions.navigateButton()
    return Button_Actions(page, helper)

@pytest.mark.button
def test_gotohomeBtn(button_actions):
    button_actions.verify_gotohomeBtn()

@pytest.mark.button
def test_disabledBtn(button_actions):
    button_actions.verify_disabledBtn()

@pytest.mark.button
def test_doubleClickBtn(button_actions):
    button_actions.verify_doubleClickBtn(ButtonData.msg_double_click)

@pytest.mark.button
def test_rightClickBtn(button_actions):
    button_actions.verify_rightClickBtn(ButtonData.msg_right_click)
    