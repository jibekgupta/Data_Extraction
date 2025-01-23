
# Product Web Scraper

This project is a web scraper that extracts product names from the "EdSurge Index" website and saves the information into a CSV file. It uses `Selenium` to automate the web browser, `BeautifulSoup` for parsing the HTML, and `webdriver_manager` to manage the Chrome WebDriver.
***
## Requirements

- Python 3.x
- `Selenium` library
- `BeautifulSoup` library (from `bs4` package)
- `webdriver_manager` library

You can install the required libraries using `pip`:

```bash
pip install selenium beautifulsoup4 webdriver-manager
```
***
## How It Works
1. The scraper navigates to the EdSurge Index website's product page: https://index.edsurge.com/products.
2. It extracts product names from the list of products on each page.
3. The script navigates through multiple pages by clicking on the 'Next' button, handling different variations of the button.
4. The scraper continues to extract product names until it reaches the maximum number of pages or encounters a page without a 'Next' button.
5. Finally, it writes the product names to a CSV file named `product_names.csv`.
***
## Features
- **Product Name Extraction**: The scraper identifies product containers and extracts their names.
- **Pagination Handling**: The scraper navigates through multiple pages of the website by interacting with the 'Next' buttons, even handling variations in the button's class name.
- **Error Handling**: The scraper includes error handling for common issues such as `ElementClickInterceptedException` and `StaleElementReferenceException`, ensuring robust navigation through pages.
- **CSV Output**: The product names are stored in a CSV file for easy access and analysis.
***
## How to Use
1. Clone the repository or copy the script to your local machine.
2. Install the required libraries by running the following command in your terminal:
   ```bash
   pip install selenium beautifulsoup4 webdriver-manager

3. Run the Python script:
   ```bash
   python product_scraper.py
4. The scraper will start extracting product names and will save the results in a `product_names.csv` file in the same directory.
***
## Notes
- Ensure that you have a compatible version of the Chrome browser installed, as the script uses the Chrome WebDriver.
- The script may need to be adjusted if the structure of the target website changes (e.g., changes to class names or page layout).
- You can adjust the `max_pages` variable in the script to control how many pages the scraper will scrape.
***
## License
This project is licensed under the MIT License - see the LICENSE file for details.
``` arduino

This `README.md` outlines the purpose, requirements, installation steps, and usage of your web scraper project, and also provides clear guidance for potential users and contributors.
```
  
