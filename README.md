# Laptop Scraper for Thegioididong.com

## Overview
This Python script is designed to scrape laptop product information from thegioididong.com, a popular Vietnamese electronics retailer. The scraper collects data such as product names, prices, RAM, SSD capacity, ratings, and sales volume, then saves this information to a CSV file for further analysis.

## Prerequisites
To run this scraper, you need:
- Python 3.x
- Selenium WebDriver
- Chrome browser
- ChromeDriver compatible with your Chrome version

## Installation
1. Install Python dependencies:
```bash
pip install selenium
```

2. Download ChromeDriver from https://chromedriver.chromium.org/downloads
   - Make sure the ChromeDriver version matches your Chrome browser version
   - Place ChromeDriver in the directory specified in the script or update the path

## Usage
Run the script with Python:
```bash
python laptop_scraper.py
```

The script will:
1. Open Chrome and navigate to thegioididong.com/laptop
2. Click "Xem thêm" (See more) buttons to load all available products
3. Extract information from each product listing
4. Save the data to `laptops.csv` in the current directory

## Output
The script generates a CSV file with the following columns:
- Tên (Name)
- Giá (Price)
- RAM
- SSD
- Rating
- Đã bán (Units sold)

## Customization
- To scrape different product categories, modify the URL in `driver.get()`
- Adjust the sleep timers (`time.sleep()`) if necessary based on your connection speed

## Troubleshooting
If you encounter errors:
- Verify your ChromeDriver path is correct
- Ensure ChromeDriver version matches your Chrome browser version
- Check if the website structure has changed, which may require updating the CSS selectors

## Legal Notice
This script is for educational purposes only. Always review and comply with the website's terms of service before scraping. Consider implementing rate limiting to avoid overloading the server.
