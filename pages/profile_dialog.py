from playwright.sync_api import Page, expect
import random

class ProfileDialog:
    def __init__(self, page: Page):
        self.page = page
        self.edit_button = page.get_by_test_id("editAvatar")
        self.nickname_input = page.get_by_test_id("nicknameInput")
        self.nickname_display = page.get_by_test_id("nicknameDisplay")
        self.apply_button = page.get_by_role("button", name="Apply")
        self.close_button = page.get_by_test_id("closeButton")

    def choose_random_avatar(self):
        """Select a random avatar from available options"""
        avatar_number = random.randint(0, 19)
        avatar = self.page.get_by_test_id(f"avatar-image-{avatar_number}")
        expect(avatar).to_be_visible()
        avatar.click()
    
    def update_profile(self, new_nickname: str):
        expect(self.edit_button).to_be_visible()
        self.edit_button.click()
        
        expect(self.nickname_input).to_be_visible()
        self.nickname_input.clear()
        self.nickname_input.fill(new_nickname)
        
        self.choose_random_avatar()
        expect(self.apply_button).to_be_enabled()
        self.apply_button.click()
        expect(self.nickname_display).to_have_text(new_nickname)

    def close_dialog(self):
        expect(self.close_button).to_be_visible()
        self.close_button.click()
