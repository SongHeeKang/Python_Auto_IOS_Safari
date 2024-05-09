from behave import when, then


# @when('메인 페이지에서 새로고침 클릭한다.')
# def step_impl(context):
#     context.mp.click_main_refresh_button()

@when('URL 입력창을 클릭한다.')
def step_impl(context):
    context.mp.click_main_url_input_bar()

@then('네이버 항공권 url 을 입력한다.')
def step_impl(context):
    context.mp.input_naver_airline_text()

@then('키보드 "go" 버튼 클릭한다.')
def step_impl(context):
    context.mp.click_keboard_go_button()

@then('네이버 항공권 페이지로 이동한다.')
def step_impl(context):
    context.mp.check_travel_products_text()