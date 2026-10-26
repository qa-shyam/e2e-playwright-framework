"""Login E2E tests using Page Object Model."""
import pytest
from pages.login_page import LoginPage
from pages.open_account_page import OpenAccountPage


@pytest.mark.smoke
def test_valid_login(page, base_url):
    """Test successful login with valid credentials."""
    login = LoginPage(page)
    login.goto().login("john", "demo").expect_success()


@pytest.mark.smoke
def test_invalid_login(page, base_url):
    """Test login failure with invalid credentials."""
    login = LoginPage(page)
    login.goto().login("bad", "creds").expect_error("The username and password could not be verified.")


@pytest.mark.regression
@pytest.mark.parametrize("user,pwd", [
    ("john", "demo"),
])
def test_multiple_users(page, base_url, user, pwd):
    """Test login with multiple user accounts."""
    LoginPage(page).goto().login(user, pwd).expect_success()


@pytest.mark.regression
def test_open_new_savings_account(page, base_url):
    """Test opening a new savings account."""
    # Login first
    login = LoginPage(page)
    login.goto().login("john", "demo").expect_success()
    
    # Click Open New Account link
    page.click('a:has-text("Open New Account")')
    page.wait_for_load_state("networkidle")
    
    # Open new savings account
    open_account = OpenAccountPage(page)
    open_account.select_account_type("SAVINGS") \
                .select_from_account("13344") \
                .click_open_new_account() \
                .expect_success()