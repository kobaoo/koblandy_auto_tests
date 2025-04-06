import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

class SimpleYouTubeSearchTest(unittest.TestCase):
    """Простой тест поиска на YouTube"""
    
    @classmethod
    def setUpClass(cls):
        """Настройка драйвера"""
        options = Options()
        options.headless = False
        
        service = Service(GeckoDriverManager().install())
        cls.driver = webdriver.Firefox(service=service, options=options)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)
        
        # Открываем YouTube
        cls.driver.get("https://www.youtube.com")

    def test_search_returns_results(self):
        """Проверка, что поиск возвращает результаты"""
        try:
            # Пропускаем окно с куки, если появится
            try:
                accept_button = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Accept all")]'))
                )
                accept_button.click()
            except:
                pass
            
            # Вводим запрос в поиск
            search_box = self.wait.until(
                EC.presence_of_element_located((By.NAME, "search_query"))
            )
            search_box.send_keys("Python tutorial" + Keys.RETURN)
            
            # Проверяем, что есть хотя бы один результат
            results = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-video-renderer"))
            )
            
            # Простая проверка - если есть хотя бы 1 результат, тест пройден
            self.assertTrue(len(results) > 0, "Поиск не вернул результатов")
            
        except Exception as e:
            self.fail(f"Тест завершился с ошибкой: {str(e)}")

    @classmethod 
    def tearDownClass(cls):
        """Завершение работы"""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()