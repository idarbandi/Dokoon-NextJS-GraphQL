"""
********************************************************************************
 * 🌐 Dokoon-NextJS-GraphQL
 * 👤 Author: idarbandi
 * 📁 GitHub: https://github.com/idarbandi/Dokoon-NextJS-GraphQL
 * ✉️ Email: darbandidr99@gmail.com
 * 💼 LinkedIn: https://www.linkedin.com/in/amir-darbandi-72526b25b/
 *
 * This project was developed by idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 ********************************************************************************
"""

# این اسکرین شات‌گیر ابزاری برای گرفتن اسکرین شات از صفحات وب‌سایت‌های مختلف است

# کتابخانه‌های مورد نیاز
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def dokoon_take_screenshots(base_url, pages, output_dir="screenshots"):
    """
    این تابع اسکرین شات از صفحات مشخص‌شده یک وب‌سایت می‌گیرد.

    Args:
        base_url(str): آدرس پایه وب‌سایت (مثال: "http://localhost:3000").
        pages(list): لیستی از مسیرهای صفحات (مثال: ["/", "/login", "/products/1"]).
        output_dir(str, optional): مسیر خروجی برای ذخیره اسکرین شات‌ها. مقدار پیش‌فرض "screenshots" است.
    """

    os.makedirs(output_dir, exist_ok=True)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    try:
        for page in pages:
            url = base_url + page
            driver.get(url)

            try:
                element_present = EC.presence_of_element_located(
                    (By.TAG_NAME, 'body'))
                WebDriverWait(driver, 10).until(element_present)
            except:
                print(
                    f"صفحه {url} زمان زیادی برای بارگذاری نیاز دارد یا عنصر مورد نظر یافت نشد. با این حال، اسکرین شات گرفته می‌شود.")

            filename = os.path.join(
                output_dir, page.replace("/", "_") + ".png")
            driver.save_screenshot(filename)
            print(f"اسکرین شات ذخیره شد: {filename}")
            time.sleep(2)

    except Exception as e:
        print(f"خطایی رخ داد: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    base_url = "http://localhost:3000"
    pages_to_capture = [
        "/",
        "/login",
        "/products/1",
        "/dashboard",
        "/category/some-category"
    ]
    dokoon_take_screenshots(base_url, pages_to_capture)

    base_url_backend = "http://localhost:8000"
    pages_to_capture_backend = [
        "/admin/",
        "/account/login/",
        "/account/logout/",
    ]
    dokoon_take_screenshots(base_url_backend, pages_to_capture_backend)
