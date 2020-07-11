import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        self.driver.maximize_window()

    def test_get_cookie(self):
        time.sleep(15)
        cookies = self.driver.get_cookies()
        print(cookies)
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)
        time.sleep(10)

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            # if "expiry" in cookie.keys():
            #     # dict支持pop的删除函数
            #     cookie.pop("expiry")
            # 添加一个dict(字典)的cookie信息，把cookie键值对一个一个的塞进浏览器
            self.driver.add_cookie(cookie)
        time.sleep(15)
        # 刷新
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            if res is not None:
                break

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")))

        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "js_upload_file_input")))
        # send_key()需要绝对路径
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys(
            "/Users/chenglin/PycharmProjects/test_cookie/test_selenium/data/workbook.xlsx")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "upload_file_name")))
        assert_ele = self.driver.find_element(By.ID, "upload_file_name").text

        assert assert_ele == "workbook.xlsx"
        time.sleep(3000)

    def teardown(self):
        self.driver.quit()
