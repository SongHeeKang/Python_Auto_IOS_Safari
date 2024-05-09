## Main
# url 입력 창
main_url_input_bar = '//XCUIElementTypeOther[@name="CapsuleViewController"]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]'

# url 입력 상세 창
main_url_input_bar_detail = '//XCUIElementTypeTextField[@name="URL"]'

# keyboard go button
search_keyboard_go_button = '//XCUIElementTypeButton[@name="Go"]'

# 네이버 항공권 메인 페이지 상단 '여행상품' 메뉴
travel_products_top_menu = '//XCUIElementTypeLink[@name="여행상품"]'


## Place
# 출발지를 선택한다.
starting_place_pointing = '//XCUIElementTypeButton[@name="ICN 인천"]'

# 검색창에서 "인천"을 검색한다.
search_bar = '//XCUIElementTypeOther[@name="SafariWindow?View=Narrow&BarsKeptMinimized=false&UUID=63F496B1-21DB-431C-A676-EA2BD119E42D&SupportsTabBar=true&UsingLoweredBar=true&UsingUnifiedBar=false"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]'
start_search_bar_detail = '//XCUIElementTypeTextField[@value="국가, 도시, 공항명 검색"]'

# 리스트 첫 번째 인천 결과를 선택한다.
start_search_list_first_result = '(//XCUIElementTypeStaticText[@name="인천"])[1]'

# 도착지를 선택한다.
ending_place_pointing = '//XCUIElementTypeButton[@name="도착 선택"]'

# 검색창에서 "도쿄"를 검색한다.
end_search_bar_detail = '//XCUIElementTypeTextField[@value="국가, 도시, 공항명 검색"]'

# 리스트 첫 번째 도쿄 결과를 선택한다.
end_search_list_first_result = '(//XCUIElementTypeStaticText[@name="도쿄"])[1]'

# start day
start_day_button = '//XCUIElementTypeButton[@name="가는 날"]'

# Recommended schedule
recommended_schedule_button = '//XCUIElementTypeOther[@name="SafariWindow?View=Narrow&BarsKeptMinimized=false&UUID=63F496B1-21DB-431C-A676-EA2BD119E42D&SupportsTabBar=true&UsingLoweredBar=true&UsingUnifiedBar=false"]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther[3]'