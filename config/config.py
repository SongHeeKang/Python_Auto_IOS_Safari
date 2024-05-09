import os
BASE_DIR = os.getcwd()


# BasePage
WAIT_TIME = 10
PASS_SCREENSHOT = True

# appium
APP_FILE = "app.ipa"
URL = 'http://127.0.0.1:4723'
PLATFORM_NAME = "ios"
PLATFORM_VERSION = "17.4"
AUTOMATION_NAME = "XCUITest"
# UDID = "AF113F2E-132E-41FC-B130-681CE1BE6F18"
UDID = "0F4EE260-E3E3-4DB5-A26F-1F4A7E315E6D"
BUNDLE_ID="com.apple.mobilesafari"
# XCODE_ORG_ID="G476VT3T47"


# threshold
# CONFIDENCE_THRESHOLD = 99.0
# DISTANCE_THRESHOLD = 0.3338
# ID_VERIFICATION_THRESHOLD = 1.0


# google
#https://console.cloud.google.com/apis/credentials 의 서비스 계정등록된 Json 파일 구글 문서에 권한을 추가해줘야함.(googleqaapi@alchera-d0790.iam.gserviceaccount.com)
# GOOGLE_AUTH_FILE_NAME= BASE_DIR + "/config/alchera-auth.json"
# GOOGLE_SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1_OPFRQ_e6OflL_VZZL5__lvafh_pKH5Mv85PYLbFxX4/edit#gid=0"
# GOOGLE_WORKSHEET="Result"