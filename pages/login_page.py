from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.get_by_test_id("lobby-login-btn")
        self.email_input = page.get_by_test_id("email-input")
        self.password_input = page.get_by_test_id("password-input")
        self.submit_button = page.get_by_test_id("login-submit-btn").get_by_role("button", name="Log in")
        self.later_button = page.get_by_role("button", name="Later")

    def login(self, email: str, password: str):
        expect(self.login_button).to_be_visible()
        self.login_button.click()
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        
        self.email_input.fill(email)
        self.password_input.fill(password)
        
        expect(self.submit_button).to_be_enabled()
        self.submit_button.click()
        
        # Handle the "Later" popup
        self.later_button.click()

