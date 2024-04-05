from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import pandas as pd
import time

# Inisialisasi WebDriver (Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--disable-infobars')
# Menggunakan undetected chromedriver
driver = uc.Chrome(options=options)
driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36"})

driver.get("https://www.importyeti.com/login")

username_input = driver.find_element(By.ID,"user_email")
password_input = driver.find_element(By.ID,"password")
login_button = driver.find_element(By.ID,"send_profile")

username_input.send_keys("leifjenkins.id@gmail.com")
password_input.send_keys("Importyeti123/")

# Klik tombol login
login_button.click()
time.sleep(5)

data=[]
for i in range(1,100, 1):
    driver.get(f"https://www.importyeti.com/search?page={i}&q=Home+Decor")
    time.sleep(5)
    wait = WebDriverWait(driver, 100)
    links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href^="/company/"], a[href^="/supplier/"]')))
    
    for link in links:
        data.append(link.get_attribute("href"))
         # Simpan link dalam file CSV
        df = pd.DataFrame({'Links': data})
        df.to_csv('homedecor.csv', index=False)

# Close the browser
driver.quit()