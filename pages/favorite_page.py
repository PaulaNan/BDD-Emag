from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FavoritePage(BasePage):

    FAVORITE_BTN_CLICK = (By.ID, 'my_wishlist')

    def click_favorite_link(self):
        self.driver.find_element(*self.FAVORITE_BTN_CLICK).click()

    def verify_url_page(self):
        self.verify_page_url('https://www.emag.ro/favorites?ref=ua_favorites')
