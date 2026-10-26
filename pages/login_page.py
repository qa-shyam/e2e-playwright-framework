"""Login Page Object Model for ParaBank."""
import re
from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object for the ParaBank login page."""

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator('input[name="username"]')
        self.password = page.locator('input[name="password"]')
        self.submit = page.locator('input[type="submit"]')
        self.error_msg = page.locator('.error, .errorMessage, [class*="error"]')

    def goto(self) -> "LoginPage":
        """Navigate to the login page."""
        self.page.goto("/")
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """Fill in credentials and submit."""
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()
        return self

    def expect_error(self, message: str) -> "LoginPage":
        """Assert that an error message is displayed."""
        expect(self.error_msg).to_contain_text(message)
        return self

    def expect_success(self) -> "LoginPage":
        """Assert successful login (redirect to overview page)."""
        expect(self.page).to_have_url(re.compile(r".*overview\.htm.*"))
        return self