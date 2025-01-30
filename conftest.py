import pytest
from playwright.sync_api import Page
from typing import Generator
import random
import string

DEFAULT_VIEWPORT = {"width": 1920, "height": 1080}
BASE_URL = "https://app.dev.crowncoinscasino.com/"
USERNAME_LENGTH = 8

@pytest.fixture(scope="function")
def page(browser) -> Generator[Page, None, None]:
    page = browser.new_page()
    page.set_viewport_size(DEFAULT_VIEWPORT)
    page.goto(BASE_URL)
    yield page
    page.close()

@pytest.fixture
def random_username() -> str:
    """
    Generates a random username for testing
    """
    return ''.join(random.choices(
        string.ascii_lowercase + string.digits, 
        k=USERNAME_LENGTH
    ))
