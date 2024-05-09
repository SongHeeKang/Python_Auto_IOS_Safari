import pages.PageElements as pe
import utilities.CustomLogger as cl
from base.BasePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
import time


class PlacePage(BasePage):

    def __init__(self, driver, context):
        super().__init__(driver, context)
        self.driver = driver
        self.context = context
        self.url = "https://flight.naver.com"
        self.start_text = "인천"
        self.end_text = "도쿄"
        
    def click_starting_place_pointing(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.starting_place_pointing)
        cl.allure_logs("출발지 선택")
        
    def input_start_search_bar_detail(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.search_bar)
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.start_search_bar_detail)
        BasePage.send_key_element(self, AppiumBy.XPATH, pe.start_search_bar_detail, self.start_text)
        cl.allure_logs(f"검색 필드에 \"{self.start_text}\" 입력")

    def click_start_search_list_first_result(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.start_search_list_first_result)
        cl.allure_logs("리스트 첫 번째 인천 결과를 선택")

    def click_ending_place_pointing(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.ending_place_pointing)
        cl.allure_logs("도착지 선택")

    def input_ending_place_pointing(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.search_bar)
        BasePage.is_displayed(self, AppiumBy.XPATH, pe.end_search_bar_detail)
        BasePage.send_key_element(self, AppiumBy.XPATH, pe.end_search_bar_detail, self.end_text)
        cl.allure_logs(f"검색 필드에 \"{self.end_text}\" 입력")

    def click_end_search_list_first_result(self):
        BasePage.click_element(self, AppiumBy.XPATH, pe.end_search_list_first_result)
        cl.allure_logs("리스트 첫 번째 도쿄 결과를 선택")




    # def click_keboard_go_button(self):
    #     BasePage.is_displayed(self, AppiumBy.XPATH, pe.search_keyboard_go_button)
    #     BasePage.click_element(self, AppiumBy.XPATH, pe.search_keyboard_go_button)
    #     cl.allure_logs("키보드 'go' 버튼 클릭")

    # def check_travel_products_text(self):
    #     BasePage.is_displayed(self, AppiumBy.XPATH, pe.travel_products_top_menu)
    #     cl.allure_logs("상단 '여행상품' 텍스트 문구 표시 확인")