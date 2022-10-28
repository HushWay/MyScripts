from matplotlib.pyplot import close
from selenium import webdriver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

########################################################
# ' 函数
#######################2022-10-27#######################
# 重命名下载的文件（selenium无法做到，因此直接查找最新的文件来重命名）


def tiny_file_rename(newname, folder_of_download, time_to_wait=60):
    time_counter = 0
    filename = max([f for f in os.listdir(folder_of_download)],
                   key=lambda xa:   os.path.getctime(os.path.join(folder_of_download, xa)))
    while '.part' in filename:
        time.sleep(1)
        time_counter += 1
        if time_counter > time_to_wait:
            raise Exception('Waited too long for file to download')
    filename = max([f for f in os.listdir(folder_of_download)],
                   key=lambda xa:   os.path.getctime(os.path.join(folder_of_download, xa)))
    os.rename(os.path.join(folder_of_download, filename),
              os.path.join(folder_of_download, newname))


def fetchPDF(PMID, file_name):
    driver.get("https://pm.yuntsg.com/searchList.html")
    search_box = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "keyWord")))
    search_box.clear()
    search_box.send_keys(PMID)
    driver.find_element_by_class_name("searchBtn").click()

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//ul[@class='tabOperation']//li[contains(text(),'申请全文')]"))).click()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='listTab']//a[1]"))).click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'保存PDF')]"))).click()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    tiny_file_rename(file_name, download_path)


#######
# ' 下载路径配置
#######
current_dir = os.path.dirname(os.path.abspath(__file__))
# current_dir = "D:\\MyPythonScripts\\泉方下载文献"
download_path = os.path.join(current_dir, "papers")

#######
# ' 配置浏览器，后台静默运行
#######
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
option.add_argument('--start-maximized')
options.add_experimental_option('prefs', {
    # Change default directory for downloads
    "download.default_directory": download_path,
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": True,
    # It will not show PDF directly in chrome
    "plugins.always_open_pdf_externally": True
})
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#######
# ' 登陆
#######
driver.get("https://user.tsgyun.com/user/login?isOffWebsite=true")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.ID, "username"))).send_keys("18845181393")
driver.find_element_by_id("password1").send_keys("liuwei78")
captcha = input("Enter CAPTCHA and Press ENTER\n")
driver.find_element_by_id("code1").send_keys(captcha)
driver.find_element_by_xpath(
    "(//button[@class='layui-btn layui-btn-fluid'][contains(text(),'登 录')])[1]").click()

#######
# ' 下载文献
#######
paper_fn = os.path.join(current_dir, "papers.txt")
paper = open(paper_fn)
Lines = paper.readlines()
for line in Lines:
    line = Lines[1]
    source = line.strip().split("\t")
    PMID = source[0]
    file_name = source[1]
    print(source)
    try:
        fetchPDF(PMID=PMID, file_name=file_name)
    except:
        pass
