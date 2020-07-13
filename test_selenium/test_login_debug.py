from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin:
    def test_debug_login(self):
        option = Options()
        # Google\ Chrome --remote-debugging-port = 9222
        # 需要和启动命令的端口号一致
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
