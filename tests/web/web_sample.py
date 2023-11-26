from src.web.pages.login_page import LoginPage
from src.web.pages.home_page import HomePage
from utils.webdriver_manager import WebDriverManager
from utils.config_reader import ConfigReader

def test_login():
       config = ConfigReader()
       username = config.get_value("Credentials", "username")
       password = config.get_value("Credentials", "password")

       # Initialize WebDriver
       web_driver = WebDriverManager().get_driver()

       # Initialize Pages
       login_page = LoginPage(web_driver)
       home_page = HomePage(web_driver)

       # Test Steps
       login_page.login(username, password)
       home_page.navigate_to_dashboard()

       # Assertions
       # Add assertions as needed

       # Clean up
       web_driver.quit()