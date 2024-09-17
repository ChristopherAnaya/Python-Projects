from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome WebDriver (this will automatically download the necessary ChromeDriver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the website
driver.get("https://flippybitandtheattackofthehexadecimalsfrombase16.com/")

# Keep the browser open for 10 seconds before quitting
driver.implicitly_wait(10)
driver.quit()
