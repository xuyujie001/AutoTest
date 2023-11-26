from selenium import webdriver


class WebDriverManager:
    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser")

    def get_driver(self):
        return self.driver