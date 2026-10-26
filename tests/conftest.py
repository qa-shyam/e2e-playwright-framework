"""Shared pytest fixtures for Playwright E2E tests."""
import pytest
from playwright.sync_api import Page, BrowserContext


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context for all tests."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "record_video_dir": "videos/",
        "ignore_https_errors": True,
    }


@pytest.fixture
def page(context: BrowserContext) -> Page:
    """Create a new page for each test."""
    page = context.new_page()
    page.set_default_timeout(30000)
    yield page
    page.close()


# Base URL from environment variable or default
@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application under test."""
    import os
    return os.getenv("BASE_URL", "https://parabank.parasoft.com/parabank/login.html")