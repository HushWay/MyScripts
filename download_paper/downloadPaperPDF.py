# TODO: 使用说明
# ...

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os

#### 配置 webdriver ####
def configChromeDriver(download_path):
    option = webdriver.ChromeOptions()
    option.add_experimental_option('prefs', {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,  # 取消下载确定
        "download.directory_upgrade": True,    
        "plugins.always_open_pdf_externally": True # 不使用chrome打开pdf
    })
    driver = webdriver.Chrome(options=option)
    return driver
current_dir = os.path.dirname(os.path.abspath(__file__))
# current_dir = "D:\\OneDrive - hrbmu.edu.cn\\workspace\\MyScripts\\泉方下载文献"
download_path = os.path.join(current_dir, "papers")
driver = configChromeDriver(download_path=download_path)

#### 登陆泉方账号 ####
def inputByID(driver, id, value):
    ele = driver.find_element(By.ID, id)
    ele.clear()
    ele.send_keys(value)

def logQuanFang(username = "2628201733@qq.com", password = "liuwei78"):
    driver.get("https://user.tsgyun.com/user/login?isOffWebsite=true")
    inputByID(driver, "username", username)
    inputByID(driver, "password1", password)

logQuanFang()
# TODO: 手动输入验证码
print("请在10秒内完成验证并点击确定...")
sleep(10)

#### 检索文献 ####
def searchPMID(driver, pmid):
    switchWindow(driver, 0)
    driver.get("https://pm.yuntsg.com/searchList.html")
    sleep(5)
    inputByID(driver, "keyWord", pmid)
    driver.find_element(By.CLASS_NAME, "searchBtn").click()

def switchWindow(driver, index):
    driver.switch_to.window(driver.window_handles[index])

def applyFirstPDF(driver):
    driver.find_element(By.XPATH, "//ul[@class='tabOperation']//li[contains(text(),'申请全文')]").click()
    driver.find_element(By.XPATH, "//div[@class='listTab']//a[1]").click()

def downloadPDF(driver):
    switchWindow(driver, 1)
    try:
        driver.execute_script("downloadPdf()")
        print("下载成功")
    except:
        print("下载失败")
    driver.close()

def downloadByPMID(driver, pmid, wait_sec = 5):
    sleep(wait_sec)
    searchPMID(driver, pmid)
    sleep(wait_sec)
    applyFirstPDF(driver)
    sleep(wait_sec*2)
    downloadPDF(driver)

#### 读取PMID列表，进行文献下载 ####
def processLine(fn,f,*args, retry_count = 1):
    file = open(fn)
    lines = file.readlines()

    for item in lines:
        pmid = item.strip()
        print(pmid)
        retry_indx = 0
        while retry_indx <= retry_count:
            try:
                f(*args, pmid)
                break # 成功的话跳出
            except Exception as e:
                print(f"Error processing {pmid}:{e}")
                if retry_indx <= retry_count:
                    print("重试中...")
                    retry_indx += 1
                else:
                    print("重试失败. 跳过。")
                    break

paper_fn = os.path.join(current_dir, "papers.txt")
processLine(paper_fn, downloadByPMID, driver)