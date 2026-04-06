from PyPlaywight.src.common.base.base import BasePage
import pytest
from PyPlaywight.actions.button.button_actions import Button_Actions

@pytest.mark.button
def test_gotohomeBtn(page, helper):
    button_actions = Button_Actions(page, helper)
    base_actions = BasePage(page, helper)
    base_actions.goto_base()
    base_actions.navigateButton()
    button_actions.verify_gotohomeBtn()

@pytest.mark.button
def test_disabledBtn(page, helper):
    button_actions = Button_Actions(page, helper)
    base_actions = BasePage(page, helper)
    base_actions.goto_base()
    base_actions.navigateButton()
    button_actions.verify_disabledBtn()

@pytest.mark.button
def test_doubleClickBtn(page, helper):
    button_actions = Button_Actions(page, helper)
    base_actions = BasePage(page, helper)
    base_actions.goto_base()
    base_actions.navigateButton()
    button_actions.verify_doubleClickBtn()

@pytest.mark.button
def test_rightClickBtn(page, helper):
    button_actions = Button_Actions(page, helper)
    base_actions = BasePage(page, helper)
    base_actions.goto_base()
    base_actions.navigateButton()
    button_actions.verify_rightClickBtn()
    