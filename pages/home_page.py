from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.menu_button = page.get_by_test_id("menuButton")
        self.my_account_button = page.get_by_role("button", name="My Account")
        self.coin_balance_button = page.get_by_role("button", name="Coin Balance")
        self.coin_balance_value = page.get_by_test_id("coinBalanceValue")
        self.lobby_balance_bar = page.get_by_test_id("lobby-balance-bar")
        self.social_coin_button = page.get_by_test_id("coin-switcher").get_by_role("img", name="Social Coin")
        self.sweep_coin_button = page.get_by_test_id("coin-switcher").get_by_role("img", name="Sweep Coin")

    def open_my_account(self):
        expect(self.menu_button).to_be_visible()
        self.menu_button.click()
        expect(self.my_account_button).to_be_visible()
        self.my_account_button.click()

    def get_lobby_balance(self):
        expect(self.lobby_balance_bar).to_be_visible()
        return self.lobby_balance_bar.text_content()
    
    def switch_to_social_coin(self):
        expect(self.social_coin_button).to_be_visible()
        self.social_coin_button.click()

    def switch_to_sweep_coin(self):
        expect(self.sweep_coin_button).to_be_visible()
        self.sweep_coin_button.click()

    def get_coin_balances(self):
        sweep_balance = self.get_lobby_balance()
        self.switch_to_social_coin()
        expect(self.lobby_balance_bar).to_be_visible()
        social_balance = self.get_lobby_balance()
        self.switch_to_sweep_coin()  
        return sweep_balance, social_balance

