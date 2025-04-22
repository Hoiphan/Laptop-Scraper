import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="/home/hoiphan/Documents/Selenium/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.thegioididong.com/laptop")

try:
    while True:
        try:
            see_more_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "see-more-btn"))
            )
            driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", see_more_button)
            print("Đã click nút 'Xem thêm'")
            time.sleep(2)
        except:
            print("Không còn nút 'Xem thêm'")
            break

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".container-productbox .listproduct"))
    )

    items = driver.find_elements(By.CSS_SELECTOR, ".listproduct > .item")
    print(f"Đã tìm thấy {len(items)} sản phẩm")

    # Mở file CSV để ghi
    with open("laptops.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Ghi tiêu đề
        writer.writerow(["Tên", "Giá", "RAM", "SSD", "Rating", "Đã bán"])

        for item in items:
            try:
                name = item.find_element(By.TAG_NAME, "h3").text
                price = item.find_element(By.CLASS_NAME, "price").text
            except:
                continue  # Bỏ qua nếu thiếu thông tin cơ bản

            # Xử lý phần thông tin có thể thiếu
            try:
                ram = item.find_element(By.CSS_SELECTOR, ".item-compare span:nth-child(1)").text
            except:
                ram = "N/A"

            try:
                ssd = item.find_element(By.CSS_SELECTOR, ".item-compare span:nth-child(2)").text
            except:
                ssd = "N/A"

            try:
                rating = item.find_element(By.CSS_SELECTOR, ".vote-txt b").text
            except:
                rating = "N/A"

            try:
                sold_text = item.find_element(By.CSS_SELECTOR, ".rating_Compare span").text
                sold = sold_text.replace("• Đã bán", "").strip()
            except:
                sold = "N/A"

            print(f"{name} - {price} | RAM: {ram} | SSD: {ssd} | ⭐ {rating} | Đã bán: {sold}")

            # Ghi vào file CSV
            writer.writerow([name, price, ram, ssd, rating, sold])

finally:
    time.sleep(3)
    driver.quit()
