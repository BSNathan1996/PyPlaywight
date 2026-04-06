import os
from pathlib import Path
from PyPlaywight.src.pages.button.button import ButtonPage
from dotenv import load_dotenv
from playwright.sync_api import Page
from PyPlaywight.src.common.helper.helper import Helper

class BasePage:
    def __init__(self, page: Page, helper: Helper) -> None:
        self.page = page
        self.helper = helper
        self.base_url = self._load_base_url()

    @staticmethod
    def _load_base_url() -> str:
        env_path = Path(__file__).resolve().parents[3] / ".env"
        load_dotenv(env_path)
        base_url = os.getenv("BASE_URL", "").strip()
        if not base_url:
            raise ValueError("BASE_URL must be set in the .env file")
        return base_url

    def goto_base(self) -> None:
        self.page.goto(self.base_url)

    def navigateButton(self):
        self.helper.click(ButtonPage.button_card)
        self.page.wait_for_url(f"{self.base_url}/buttons")