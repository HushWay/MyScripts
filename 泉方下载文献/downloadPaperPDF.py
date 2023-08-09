from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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
download_path = "D:/OneDrive - hrbmu.edu.cn/workspace/MyScripts/泉方下载文献/papers"
driver = configChromeDriver(download_path=download_path)

#### 登陆泉方账号 ####
def inputByID(driver, id, value):
    ele = driver.find_element(By.ID, id)
    ele.clear()
    ele.send_keys(value)

def logQuanFang(username = "18846116416", password = "liuwei78"):
    driver.get("https://user.tsgyun.com/user/login?isOffWebsite=true")
    inputByID(driver, "username", username)
    inputByID(driver, "password1", password)

logQuanFang()
# TODO: 输入验证码

#### 检索文献 ####
def searchPMID(driver, pmid):
    driver.get("https://pm.yuntsg.com/searchList.html")
    inputByID(driver, "keyWord", pmid)
    driver.find_element(By.CLASS_NAME, "searchBtn").click()

def switchWindow(driver, index):
    driver.switch_to.window(driver.window_handles[index])

def applyFirstPDF(driver):
    driver.find_element(By.XPATH, "//ul[@class='tabOperation']//li[contains(text(),'申请全文')]").click()
    driver.find_element(By.XPATH, "//div[@class='listTab']//a[1]").click()
    switchWindow(driver, 0)

def downloadPaper(driver, pmid):


pmid = 36289336
searchPMID(driver, pmid)
