from playwright.async_api import Page

class Authenticator:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self, page):
        """Handles the login process using Google authentication."""
        try:
            page.goto('https://myaccount.google.com')
            if "Welcome" in page.content():
                print("Already logged in, skipping login.")
                return True
            else:
                print("Not logged in, proceeding with login...")
                page.goto('https://accounts.google.com/')
                page.fill('input[type="email"]', self.email)
                page.click('#identifierNext')
                page.wait_for_selector('input[type="password"]', timeout=10000)
                page.fill('input[type="password"]', self.password)
                page.click('#passwordNext')
                page.wait_for_load_state('networkidle')
                print("Login successful.")
                return True
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return False


class AsyncAuthenticator:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    async def login(self, page: Page):
        """Handles the login process using Google authentication."""
        try:
            await page.goto('https://myaccount.google.com')
            content = await page.content()
            if "Welcome" in content:
                print("Already logged in, skipping login.")
                return True
            else:
                print("Not logged in, proceeding with login...")
                await page.goto('https://accounts.google.com/')
                await page.fill('input[type="email"]', self.email)
                await page.click('#identifierNext')
                await page.wait_for_selector('input[type="password"]', timeout=10000)
                await page.fill('input[type="password"]', self.password)
                await page.click('#passwordNext')
                await page.wait_for_load_state('networkidle')
                print("Login successful.")
                return True
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return False
