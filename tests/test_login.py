"""Login E2E tests using Page Object Model."""
import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_login(page, base_url):
    """Test successful login with valid credentials."""
    login = LoginPage(page)
    login.goto().login("user", "pass").expect_success()


@pytest.mark.smoke
def test_invalid_login(page, base_url):
    """Test login failure with invalid credentials."""
    login = LoginPage(page)
    login.goto().login("bad", "creds").expect_error("Invalid credentials")


@pytest.mark.regression
@pytest.mark.parametrize("user,pwd", [
    ("admin", "admin123"),
    ("user", "user123"),
])
def test_multiple_users(page, base_url, user, pwd):
    """Test login with multiple user accounts."""
    LoginPage(page).goto().login(user, pwd).expect_success()