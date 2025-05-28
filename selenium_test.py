from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Cấu hình để kết nối tới Selenium container
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

# Truy cập frontend (Angular) hoặc backend (Laravel)
driver.get("http://web:8000")  # hoặc http://web:8000 hoặc http://angular-ui:4200 nếu expose ra ngoài

print("Title:", driver.title)

# Bạn có thể tìm phần tử, kiểm tra text, click,...
# Ví dụ kiểm tra tiêu đề:
assert "Laravel" in driver.title or "Tool Shop" in driver.title

driver.quit()
