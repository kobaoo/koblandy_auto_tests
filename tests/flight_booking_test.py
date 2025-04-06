import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import time

class TestFlyArystanBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 200)
        cls.driver.get("https://flyarystan.com")
        time.sleep(2)  # Wait for initial load

    def test_book_flight_with_checkpoint(self):
        driver = self.driver
        wait = self.wait

        # 1. Accept cookies if present
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Принять все')]")))
            accept_cookies.click()
            time.sleep(2)
        except:
            pass

        # 2. Enter departure city (Almaty)
        departure_input = wait.until(EC.element_to_be_clickable((By.ID, "from")))
        departure_input.clear()
        departure_input.send_keys("Алматы")
        time.sleep(2)

        from_cities = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@id='FromCountry']//div[contains(@class, 'select-list__item')]")))
        print(f"Departure cities found: {len(from_cities)}")

        if from_cities:
            wait.until(EC.element_to_be_clickable(from_cities[1])).click()
        else:
            print("❌ No departure city found")

        # 3. Enter arrival city (Astana)
        arrival_input = wait.until(EC.element_to_be_clickable((By.ID, "to")))
        time.sleep(2)
        arrival_input.send_keys("Астана")
        time.sleep(2)

        to_cities = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@id='toCountry']//div[contains(@class, 'select-list__item')]")))
        print(f"Arrival cities found: {len(to_cities)}")

        if to_cities:
            wait.until(EC.element_to_be_clickable(to_cities[1])).click()
        else:
            print("❌ No arrival city found")

        arrival_input.send_keys(Keys.TAB)
        time.sleep(1)
        

        # Кликаем на первую доступную дату (по классу)
        first_available_date = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class, 'day') and not(contains(@class, 'disabled')) and text()='30'][1]")))
        first_available_date.click()  
        time.sleep(1)

        submit = driver.find_element(By.ID, "sButton")
        time.sleep(2)
        submit.click()
        time.sleep(2)




    #     # 5. Search for flights
    #     search_btn = wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, "//button[contains(., 'Search')]")))
    #     search_btn.click()

    #     # 6. Select the first flight
    #     wait.until(EC.presence_of_element_located(
    #         (By.XPATH, "//div[contains(@class, 'flight-item')]")))
    #     select_btn = wait.until(EC.element_to_be_clickable(
    #         (By.XPATH, "(//button[contains(., 'Select')])[1]")))
    #     select_btn.click()

    #     # 7. Enter passenger details
    #     first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
    #     first_name.send_keys("Test")

    #     last_name = driver.find_element(By.NAME, "lastName")
    #     last_name.send_keys("User")

    #     email = driver.find_element(By.NAME, "email")
    #     email.send_keys("test@example.com")

    #     phone = driver.find_element(By.NAME, "phone")
    #     phone.send_keys("77071234567")

    #     # 8. Seat selection
    #     try:
    #         seat_option = wait.until(EC.element_to_be_clickable(
    #             (By.XPATH, "//div[contains(., 'Seat Selection')]")))
    #         seat_option.click()
    #         time.sleep(1)

    #         first_seat = wait.until(EC.element_to_be_clickable(
    #             (By.XPATH, "(//div[contains(@class, 'seat-available')])[1]")))
    #         first_seat.click()
    #         print("✅ Seat successfully selected (checkpoint reached)")
    #     except Exception as e:
    #         print(f"⚠ Seat selection failed: {str(e)}")

    #     # 9. Verify navigation to payment page
    #     time.sleep(3)
    #     current_url = driver.current_url
    #     self.assertIn("payment", current_url.lower())
    #     print("✅ Successfully reached the payment page")

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
