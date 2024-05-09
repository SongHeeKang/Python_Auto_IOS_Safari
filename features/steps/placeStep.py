from behave import when, then


# @when('메인 페이지에서 새로고침 클릭한다.')
# def step_impl(context):
#     context.mp.click_main_refresh_button()

@when('출발지를 선택한다.')
def step_impl(context):
    context.pp.click_starting_place_pointing()

@then('검색창에서 "인천"을 검색한다.')
def step_impl(context):
    context.pp.input_start_search_bar_detail()

@then('리스트 첫 번째 인천 결과를 선택한다.')
def step_impl(context):
    context.pp.click_start_search_list_first_result()

@then('도착지를 선택한다.')
def step_impl(context):
    context.pp.click_ending_place_pointing()

@then('검색창에서 "도쿄"를 검색한다.')
def step_impl(context):
    context.pp.input_ending_place_pointing()

@then('리스트 첫 번째 도쿄 결과를 선택한다.')
def step_impl(context):
    context.pp.click_end_search_list_first_result()


# @then('가는 날을 선택한다.')
# def step_impl(context):
#     context.mp.check_travel_products_text()

# @then('상단 추천일정을 선택한다.')
# def step_impl(context):
#     context.mp.check_travel_products_text()

# @then('리스트 최상단 일정을 선택한다.')
# def step_impl(context):
#     context.mp.check_travel_products_text()

# @then('설정된 일정을 확인한다.')
# def step_impl(context):
#     context.mp.check_travel_products_text()