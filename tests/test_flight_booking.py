def test_flight_booking(driver):
    driver.get("https://blazedemo.com/")

    from_city = driver.find_element("name", "fromPort")
    to_city = driver.find_element("name", "toPort")

    from_city.send_keys("Boston")
    to_city.send_keys("London")

    driver.find_element("css selector", "input[type='submit']").click()

    assert "Flights from Boston to London" in driver.page_source
    driver.find_element("css selector", "input[type='submit']").click()

    driver.find_element("id", "inputName").send_keys("John Doe")
    driver.find_element("id", "address").send_keys("123 Elm Street")
    driver.find_element("id", "city").send_keys("Boston")
    driver.find_element("id", "state").send_keys("MA")
    driver.find_element("id", "zipCode").send_keys("02118")
    driver.find_element("id", "creditCardNumber").send_keys("4111111111111111")
    driver.find_element("id", "nameOnCard").send_keys("John Doe")

    driver.find_element("css selector", "input[type='submit']").click()

    assert "Thank you for your purchase today!" in driver.page_source
    assert driver.title == "BlazeDemo Confirmation"
    print("Flight booking successful!")
