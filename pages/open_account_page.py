"""Open New Account Page Object Model for ParaBank."""
from playwright.sync_api import Page, expect


class OpenAccountPage:
    """Page Object for the ParaBank Open New Account page."""

    def __init__(self, page: Page):
        self.page = page
        self.account_type = page.locator("#type")
        self.from_account = page.locator("#fromAccountId")
        self.open_button = page.locator('input[type="button"][value="Open New Account"]')

    def select_account_type(self, account_type: str) -> "OpenAccountPage":
        """Select account type (CHECKING or SAVINGS)."""
        self.account_type.select_option(label=account_type)
        return self

    def select_from_account(self, account_id: str) -> "OpenAccountPage":
        """Select existing account to transfer from."""
        self.from_account.select_option(value=account_id)
        return self

    def click_open_new_account(self) -> "OpenAccountPage":
        """Click the Open New Account button."""
        self.open_button.click()
        return self

    def expect_success(self) -> "OpenAccountPage":
        """Assert successful account creation (success message displayed)."""
        expect(self.page.locator("text=Account Opened!")).to_be_visible()
        expect(self.page.locator("text=Congratulations, your account is now open.")).to_be_visible()
        return self