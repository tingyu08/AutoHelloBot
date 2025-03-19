import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

TWITCH_URL = "https://www.twitch.tv/popout/bbbb87/chat"

TWITCH_SID = ""

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # 最大化視窗
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def login_with_cookie(driver):
    driver.add_cookie({"name": "auth-token", "value": TWITCH_SID, "domain": ".twitch.tv"})
    driver.refresh()  # 刷新頁面使 Cookie 生效
    print("✅ 使用 Cookie 自動登入 Twitch 成功！")

driver = setup_driver()
driver.get(TWITCH_URL)
login_with_cookie(driver)

def waiting_button():
    waitbtn = WebDriverWait(driver, 1)

    try:
        waitbtn.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='ScCoreButton-sc-ocjdkq-0 khjbBN']")))
        hello = driver.find_element(By.CSS_SELECTOR, "button[class='ScCoreButton-sc-ocjdkq-0 khjbBN']")
        hello.send_keys(Keys.RETURN)

    except:
        print("等待按鈕!")
        waiting_button()

def send_chat_message():
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='小奇點和點數餘額']")))
        open_label = driver.find_element(By.CSS_SELECTOR, "button[aria-label='小奇點和點數餘額']")
        open_label.send_keys(Keys.RETURN)

        # 規則
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '開始使用！')]")))
        ok_btn=driver.find_element(By.XPATH, "//button[contains(text(), '開始使用！')]")
        ok_btn.send_keys(Keys.RETURN)

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[11]/div/button")))
        hello_button = driver.find_element(By.XPATH, "//div[11]/div/button")
        hello_button.send_keys(Keys.RETURN)

        waiting_button()

    except Exception as e:
        print("發生錯誤")

    finally:
        input("按 Enter 鍵關閉瀏覽器...")
        driver.quit()

send_chat_message()