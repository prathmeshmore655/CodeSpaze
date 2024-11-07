import time
import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# Automatically install geckodriver
geckodriver_autoinstaller.install()

def scrape_weather_data(city):
    # Set up the Firefox driver
    service = Service()
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)

    try:
        # Navigate to Weather.com
        driver.get("https://weather.com")

        # Find the search box and enter the city name
        search_box = driver.find_element(By.XPATH, '//*[@id="LocationSearch_input"]')
        search_box.send_keys(city)
        search_box.submit()

        # Wait for the results to load
        time.sleep(5)  # Adjust time as needed

        # Get the temperature and weather condition
        temperature = driver.find_element(By.XPATH, '//*[contains(@class, "CurrentConditions--tempValue--3KcTQ")]')
        weather_condition = driver.find_element(By.XPATH, '//*[contains(@class, "CurrentConditions--phraseValue--2xXSr")]')

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature.text}")
        print(f"Condition: {weather_condition.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    scrape_weather_data(city_name)
