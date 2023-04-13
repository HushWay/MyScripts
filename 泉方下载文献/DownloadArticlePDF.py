from selenium import webdriver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
# option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
option.add_argument('--start-maximized')
option.add_experimental_option('prefs', {
    # Change default directory for downloads
    "download.default_directory": download_path,
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": True,
    # It will not show PDF directly in chrome
    "plugins.always_open_pdf_externally": True
})
driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)


driver.get("https://pm.yuntsg.com/searchList.html")
    sleep(2)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "keyWord"))).clear()
    sleep(1)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "keyWord"))).send_keys(PMID)