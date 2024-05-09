Feature: 사파리 메인 페이지

    Background: 초기화
        Given 테스트 수행 전 초기화한다.
    
    Scenario: 네이버 항공권 페이지 이동
        When URL 입력창을 클릭한다.
        Then 네이버 항공권 url 을 입력한다.
        Then 키보드 "go" 버튼 클릭한다.
        Then 네이버 항공권 페이지로 이동한다.

    # Scenario: 계정 로그인 무시하기
    #     When 메인 페이지에서 새로고침 클릭한다.

    # Scenario: 네이버 항공권 페이지 이동
    #     When URL 입력창을 클릭한다.
    #     Then 네이버 항공권 url 을 입력한다.
    #     Then 키보드 "go" 버튼 클릭한다.
    #     Then 네이버 항공권 페이지로 이동한다.

    # Scenario: 네이버 항공권 페이지로 이동하기
    #     When 네이버 항공권 검색 결과에서 링크 텍스트를 클릭한다.
    #     Then 네이버 항공권 페이지로 이동한다.