from selenium.webdriver.common.by import By
from src.pom.pages.base_page import BasePageElement


class HomePage(BasePageElement):
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    LOGIN_LINK = (By.XPATH, "//button[@id='doLogin']")
    USERNAME = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='doLogin']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")
    ROOM_NAME = (By.XPATH, "//input[@id='roomName']")
    ROOM_TYPE = (By.XPATH, "//select[@id='type']")
    ACCESSIBLE = (By.XPATH, "//select[@id='accessible']")
    ROOM_PRICE = (By.XPATH, "//input[@id='roomPrice']")
    ROOM_DETAILS = (By.XPATH, "//input[@id='wifiCheckbox']")
    CREATE_BUTTON = (By.XPATH, "//button[@id='createRoom']")


   def logo_is_displayed(self):
        return self.is_displayed(self.LOGIN_LINK)

 def logo_is_displayed(self):
        return self.is_displayed(self.USERNAME)

 def logo_is_displayed(self):
        return self.is_displayed(self.PASSWORD)

 def create_booking(self, Login):
        self.click((By.XPATH, Login))
    def invalid_credentails_displayed(self):
        return self.error_is_displayed(self.LOGIN_LINK)

    def invalid_credentails(self):
        return self.invalid_credentails_is_displayed(self.LOGIN_LINK)

    def room_booking(self):
        WebElements = self.find_multiple_elements(self.ROOM_NAME, self.ROOM_TYPE, self.ACCESSIBLE, self.ROOM_PRICE, self.ROOM_DETAILS)
        for element in WebElements:
            return element.is_displayed()

    def create_booking(self, Room):
        self.click((By.XPATH, Room))


