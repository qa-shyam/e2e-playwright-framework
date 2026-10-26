"""Login Page Object Model."""
from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object for the login page."""

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.submit = page.locator("button[type=submit]")
        self.error_msg = page.locator(".error-message")

    def goto(self) -> "LoginPage":
        """Navigate to the login page."""
        self.page.goto("/login")
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """Fill in credentials and submit."""
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()
        return self

    def expect_error(self, message: str) -> "LoginPage":
        """Assert that an error message is displayed."""
        expect(self.error_msg).to_have_text(message)
        return self

    def expect_success(self) -> "LoginPage":
        """Assert successful login (redirect to dashboard)."""
        expect(self.page).to_have_url("**/dashboard")
        return self