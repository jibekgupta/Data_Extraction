from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from bs4 import BeautifulSoup
import csv
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

# Function to check for different 'Next' button variations and handle disabled buttons
def get_next_button():
    try:
        # Try for a clickable button with class 'right_arrow'
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "right_arrow"))
        )
        return next_button
    except:
        pass  # If 'right_arrow' fails, try for 'dbl_right_arrow'

    try:
        # If 'right_arrow' fails, try for a clickable button with class 'dbl_right_arrow'
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "dbl_right_arrow"))
        )
        return next_button
    except:
        return None  # No next button found

page_count = 0
max_pages = 100

while page_count < max_pages:
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract product names from the current page and add to the list
    all_product_names.extend(extract_product_names(soup))

    # Find the 'Next' button using attempts for different class names
    next_button = get_next_button()
    if next_button:
        while True:
            try:
                # Try a regular click first
                next_button.click()
                break  # If click succeeds, break out of the loop
            except ElementClickInterceptedException:
                # Scroll the element into view and try clicking again
                driver.execute_script("arguments[0].scrollIntoView();", next_button)
                time.sleep(1)
            except StaleElementReferenceException:
                # Re-fetch the next button if it becomes stale
                next_button = get_next_button()
                if not next_button:
                    break
            except Exception as e:
                print(f"An unexpected exception occurred: {e}")
                break
        # Wait for the next page to load
        time.sleep(3)
        page_count += 1
    else:
        break

# Print all product names
#print(all_product_names)

# Write the product names to a CSV file
with open('product_names.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name'])
    for name in all_product_names:
        writer.writerow([name])

# Close the WebDriver
driver.quit()
