import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

class TestHerokuappLoginLogout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Настройка Firefox
        cls.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.get("https://the-internet.herokuapp.com/login")

    def test_login_logout(self):
        driver = self.driver

        # Ввод логина
        username_input = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("tomsmith")

        # Ввод пароля
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("SuperSecretPassword!")
        password_input.send_keys(Keys.RETURN)

        # Проверка успешного входа
        success_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "flash.success"))
        )
        self.assertIn("You logged into a secure area!", success_message.text)

        # Нажатие кнопки Logout
        logout_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/logout"]'))
        )
        logout_button.click()

        # Проверка, что снова на странице логина
        login_header = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )
        self.assertEqual(login_header.text.strip(), "Login Page")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
