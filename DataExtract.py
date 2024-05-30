from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set up the WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://index.edsurge.com/products"
driver.get(url)

# Function to extract product names from the current page
def extract_product_names(soup):
    product_names = []
    product_containers = soup.find_all('div', {'class': 'product'})  # Adjust class name if necessary
    for container in product_containers:
        product_name_tag = container.find('strong')
        if product_name_tag:
            product_name = product_name_tag.text.strip()
            product_names.append(product_name)
    return product_names

# Initialize an empty list to store all product names
all_product_names = []

# Function to check if a 'Next' button or '>' exists
def get_next_button():
    try:
        return WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '>')]"))
        )
    except:
        return None

while True:
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Extract product names from the current page and add to the list
    all_product_names.extend(extract_product_names(soup))
    
    # Find the 'Next' button and click it, if it exists
    next_button = get_next_button()
    if next_button:
        next_button.click()
        # Wait for the next page to load
        time.sleep(3)
    else:
        break

# Print all product names
print(all_product_names)

# Close the WebDriver
driver.quit()