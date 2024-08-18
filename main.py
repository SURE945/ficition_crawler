from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import wrapper
import convertor

chrome_options = webdriver.ChromeOptions()

# 创建Chrome浏览器实例
driver = webdriver.Chrome(options=chrome_options)

# 打开指定的网页
url = 'https://www.dynxsw.com/book/259018/'  # 替换为你要打开的网页
driver.get(url)

# 等待页面加载完成
time.sleep(2)

for i in range(1, 3):
    # 查找网页中的链接并点击（通过部分链接文本）
    idx = convertor.number_to_chinese(i)
    partial_link_text = f'第{idx}章'  # 替换为你要点击的部分链接文本
    link = driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)
    link.click()

    current_url = driver.current_url
    print("当前页面的URL是:", current_url)

    wrapper.download(driver)

    # 等待一些时间，以便观察点击后的效果
    time.sleep(5)

    driver.back()

    time.sleep(2)

time.sleep(5)

# 关闭浏览器
driver.quit()

