from playwright.sync_api import Page, Locator, TimeoutError

class Helper:
    def __init__(self, page: Page):
        self.page = page

    def _locator(self, target: str | Locator) -> Locator:
        return target if hasattr(target, "locator") is False else target

    def wait_for_selector(self, selector: str | Locator, state: str = "visible", timeout: int = 5000) -> Locator:
        locator = selector if hasattr(selector, "locator") else self.page.locator(selector)
        locator.wait_for(state=state, timeout=timeout)
        return locator

    def is_visible(self, selector: str | Locator, timeout: int = 5000) -> bool:
        try:
            locator = self.wait_for_selector(selector, state="visible", timeout=timeout)
            return locator.is_visible()
        except TimeoutError:
            return False

    def is_editable(self, selector: str | Locator, timeout: int = 5000) -> bool:
        try:
            locator = self.wait_for_selector(selector, state="visible", timeout=timeout)
            return locator.is_editable()
        except TimeoutError:
            return False

    def is_enabled(self, selector: str | Locator, timeout: int = 5000) -> bool:
        try:
            locator = self.wait_for_selector(selector, state="attached", timeout=timeout)
            return locator.is_enabled()
        except TimeoutError:
            return False
        
    def is_disabled(self, selector: str | Locator, timeout: int = 5000) -> bool:
                try:
                    locator = self.wait_for_selector(selector, state="attached", timeout=timeout)
                    return not locator.is_enabled()
                except TimeoutError:
                    return False   
                    
    def is_checked(self, selector: str | Locator, timeout: int = 5000) -> bool:
        try:
            locator = self.wait_for_selector(selector, state="attached", timeout=timeout)
            return locator.is_checked()
        except TimeoutError:
            return False

    def click(self, selector: str | Locator, timeout: int = 5000, force: bool = False, delay: int = 0) -> None:
        locator = selector if hasattr(selector, "locator") else self.page.locator(selector)
        locator.click(timeout=timeout, force=force, delay=delay)

    def fill(self, selector: str | Locator, text: str, timeout: int = 5000, clear: bool = True) -> None:
        locator = selector if hasattr(selector, "locator") else self.page.locator(selector)
        if clear:
            locator.fill(text, timeout=timeout)
        else:
            locator.type(text, timeout=timeout)

    def type_text(self, selector: str | Locator, text: str, delay: int = 50, timeout: int = 5000) -> None:
        locator = selector if hasattr(selector, "locator") else self.page.locator(selector)
        locator.type(text, delay=delay, timeout=timeout)

    def get_text(self, selector: str | Locator, timeout: int = 5000) -> str:
        locator = self.wait_for_selector(selector, state="visible", timeout=timeout)
        return locator.text_content() or ""

    def get_attribute(self, selector: str | Locator, name: str, timeout: int = 5000) -> str | None:
        locator = self.wait_for_selector(selector, state="attached", timeout=timeout)
        return locator.get_attribute(name)
    
    def select_option(self, selector: str | Locator, value: str | list[str], timeout: int = 5000) -> list[str]:
        locator = selector if hasattr(selector, "locator") else self.page.locator(selector)
        return locator.select_option(value, timeout=timeout)