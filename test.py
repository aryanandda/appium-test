from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    deviceName='Android',
    language='en',
    locale='US',
)

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Instagram').click()

# xpath_username = '//android.widget.FrameLayout[@resource-id="com.instagram.android:id/layout_container_main"]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'
# xpath_password = '//android.widget.FrameLayout[@resource-id="com.instagram.android:id/layout_container_main"]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.EditText'
#
# driver.find_element(AppiumBy.XPATH, xpath_username).send_keys('xxshv88')
# driver.find_element(AppiumBy.XPATH, xpath_password).send_keys('godblessme20')
# driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Log in"]').click()

driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Camera').click()
driver.quit()

# driver.tap()
# driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.instagram.android:id/gallery_picker_grid_item_container"])[2]')
# multi select id = com.instagram.android:id/multi_select_slide_button_alt
# image pertama xpath = //android.view.ViewGroup[@index=0]

