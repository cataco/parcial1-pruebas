import unittest
import time
from appium import webdriver


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Untitled'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = ''
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def test_order_about_menu(self):
        self.driver.find_element_by_id('android:id/button2').click()
        time.sleep(1)
        options = ['Version', "What's New", "License"]
        self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='More options']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout").click()
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.RelativeLayout").click()
        for i in range(1, 4):
            category = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/"
                                                         "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                         "android.view.ViewGroup/android.widget.FrameLayout[2]/"
                                                         "android.widget.LinearLayout/android.widget.LinearLayout/"
                                                         "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                         "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                         "android.widget.ListView/android.widget.LinearLayout[{}]/"
                                                         "android.widget.RelativeLayout/android.widget.TextView".format(
                i)).text
            self.assertEqual(category, options[i - 1])

        self.driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='Navigate up']").click()
    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()