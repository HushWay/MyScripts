#! python3
# findMagazine.py - 复制LetPub杂志信息地址，运行此脚本获取“SCI IF	出版周期	年收稿量	JCR分区	中科院分区（基础版）	中科院分区（升级版）”信息

# 加入必要的模块，没有的话先安装
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pyperclip, re

def findDisplayedElementContent(eles):
    for ele in eles:
        try:
            ele['style']
            if 'display:none' not in ele['style']:
                result = ele.text
        except:
            print("Element do not have 'style' attribute")
    return result

# 配置浏览器，后台静默运行
option = webdriver.ChromeOptions()
# I use the following options as my machine is a window subsystem linux. 
# I recommend to use the headless option at least, out of the 3
# option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
option.add_argument('--start-maximized')
# option.add_argument("user-data-dir=C:\\Users\\way\\AppData\\Local\\Google\\Chrome\\User Data")
# Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
driver = webdriver.Chrome('D://Program Files//Python//Python37//Scripts//chromedriver.exe', options=option)

# 登陆账号
driver.get("https://www.letpub.com.cn/index.php?page=login")
try:
    # WebDriverWait(driver, 0, 0.5).until(EC.presence_of_element_located((By.ID, "form")))
    sleep(1)
    print("Form showed up")
    driver.find_element_by_id("email").send_keys("2628201733@qq.com")
    driver.find_element_by_id("password").send_keys("liuwei")
except:
    print("loggin error.")
driver.execute_script("login()")
# 结束

input = pyperclip.paste().strip()
# 初始化值
publish_frequency = ""
review_period = ""
impact_factor = ""
frequency = ""
NO_articles_year = ""
SCI_partition = ""
CST_partition = ""
CST_partition_up = ""
# 如果输入不是网页地址而是杂志名的话：
if "https:" not in input:
    magazine = input
    driver.get("https://www.letpub.com.cn/index.php?page=journalapp")
    driver.refresh() # 刷新去除弹窗广告
    search = driver.find_element_by_id("searchname")
    search.clear()
    search.send_keys(magazine)
    driver.find_element_by_css_selector("input[type='submit']").click()
    soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup
    try:
        first_result = soup.findAll("table")[1].findAll('tr')[2]
        fist_magazine = first_result.find('a').text
        # row = soup.find(lambda tag:tag.name == "tr" and magazine.upper() in tag.text.upper)
        if fist_magazine.upper() != magazine.upper():
            print("Input is "+input+ ", while the first result is " +fist_magazine+ ", please check the input.")
            quit()
        else:
            # 录用比例：
            recieve_frequency = first_result.findAll("td")[8].text
            # 审稿周期
            review_period = first_result.findAll("td")[9].text
            url = "https://www.letpub.com.cn/" + str(first_result.find("a")["href"])
    except:
        print("No search result found.")
        quit()
else: # 输入为地址
    url = input

# 访问给定杂志的结果
page = driver.get(url) # Getting page HTML through request
# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table_yjfx")))  # We are waiting for 5 seconds for our element with the attribute data-testid set as `firstListCardGroup-editorial`
driver.implicitly_wait(30) # 等待页面加载完毕
driver.refresh() # 刷新去除弹窗广告 
soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup
tbody = soup.find_all("table", {"class": "table_yjfx"})[1].find('tbody')

# 提取影响因子
number_re = re.compile(r'[0-9.]+')
row = tbody.find(lambda tag:tag.name == "tr" and "最新IF" in tag.text)
impact_factor = number_re.search(row.findAll("td")[1].text).group()

# 出版周期
row = tbody.find(lambda tag:tag.name == "tr" and "出版周期" in tag.text)
frequency = row.findAll("td")[1].text

# 年文章数
row = tbody.find(lambda tag:tag.name == "tr" and "年文章数" in tag.text)
NO_articles_year = number_re.search(row.findAll("td")[1].text).group()

# SCI分区
row = tbody.find(lambda tag:tag.name == "tr" and "期刊SCI分区" in tag.text)
SCI_info = row.findAll("td")[1].findAll("tr")[1].find("td")
domain = SCI_info.findAll(text = True, recursive=False)[0]
partition = findDisplayedElementContent(SCI_info.findAll("span"))
SCI_partition = domain + partition

# 中科院分区（基础版）
row = tbody.find(lambda tag:tag.name == "tr" and "最新基础版" in tag.text)
CST_info = row.findAll("td")[1].find("td")
CST_domain = CST_info.findAll(text = True, recursive=False)[0]
CST_part = findDisplayedElementContent(CST_info.findAll("span"))
CST_partition = CST_domain + CST_part

# 中科院分区（升级版）
row = tbody.find(lambda tag:tag.name == "tr" and "最新升级版" in tag.text)
CST_info_up = row.findAll("td")[1].find("td")
CST_domain_up = CST_info_up.findAll(text = True, recursive=False)[0]
CST_part_up = findDisplayedElementContent(CST_info_up.findAll("span"))
CST_partition_up = CST_domain_up + CST_part_up

# 将结果粘到剪贴板，以\t分隔便于贴到excel中
result = '\t'.join([recieve_frequency, review_period, impact_factor, frequency, NO_articles_year, SCI_partition, CST_partition, CST_partition_up])
pyperclip.copy(result)
print("杂志名:"+ magazine +", 录用比例:" + recieve_frequency + ",审稿周期:" + review_period +', IF: ' + str(impact_factor) + ', 出版周期: ' + str(frequency) + ', 年文章数：' + str(NO_articles_year) +', SCI分区:' + SCI_partition + ', 中科院分区(基础版):' + CST_partition + ', 中科院分区(升级版)' + CST_partition_up)
driver.quit()