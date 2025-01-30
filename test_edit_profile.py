from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.profile_dialog import ProfileDialog

def test_profile_update_and_balance_check(page: Page, random_username: str):
    """
    Test profile update functionality and verify coin balances
    Steps:
    1. Login to the system
    2. Update profile with random username and avatar
    3. Verify profile updates
    4. Check coin balances for both coin types
    """
    login_page = LoginPage(page)
    home_page = HomePage(page)
    profile_dialog = ProfileDialog(page)

    login_page.login("watchdogstest02+11@sunfltd.com", "123456")
    expect(home_page.menu_button).to_be_visible()

    home_page.open_my_account()
    profile_dialog.update_profile(random_username)
    expect(profile_dialog.nickname_display).to_have_text(random_username)
    profile_dialog.close_dialog()

    sweep_balance, social_balance = home_page.get_coin_balances()
    
    # Print balances 
    print(f"Sweep Coin Balance: {sweep_balance}")
    print(f"Social Coin Balance: {social_balance}")



