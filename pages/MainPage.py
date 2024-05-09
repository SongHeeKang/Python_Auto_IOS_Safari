import pages.PageElements as pe
import utilities.CustomLogger as cl
from base.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
import time


class MainPage(BasePage):

    def __init__(self, driver, context):
        super().__init__(driver, context)
        self.driver = driver
        self.context = context
        self.text = "네이버 항공권"
        self.url = "https://flight.naver.com"
        
    def click_main_url_input_bar(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.main_url_input_bar)
        cl.allure_logs("URL 입력창을 클릭")
        
    def input_naver_airline_text(self):
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.main_url_input_bar_detail)
        BasePage.send_key_element(self, AppiumBy.XPATH, pe.main_url_input_bar_detail, self.url)
        cl.allure_logs(f"검색 필드에 \"{self.url}\" 입력")

    def click_keboard_go_button(self):
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.search_keyboard_go_button)
        BasePage.click_element(self, AppiumBy.XPATH, pe.search_keyboard_go_button)
        cl.allure_logs("키보드 'go' 버튼 클릭")

    def check_travel_products_text(self):
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.travel_products_top_menu)
        cl.allure_logs("상단 '여행상품' 텍스트 문구 표시 확인")