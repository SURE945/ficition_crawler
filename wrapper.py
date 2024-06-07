from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def download(driver):
    # 获取页面的HTML内容
    html_content = driver.page_source

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找目标<div>元素
    wrapper_div = soup.find('div', id='wrapper')
    content_text = ""
    title = ""

    if wrapper_div:
        content_read_div = wrapper_div.find('div', class_='content_read')
        if content_read_div:
            content_div = content_read_div.find('div', id='content')
            if content_div:
                # 获取<div id="content">中的文本内容
                content_text = content_div.get_text()

    if wrapper_div:
        content_read_div = wrapper_div.find('div', class_='content_read')
        if content_read_div:
            bookname_div = content_read_div.find('div', class_='bookname')
            if bookname_div:
                title_element = bookname_div.find('h1')
                if title_element:
                    title = title_element.get_text(strip=True)


    # 将标题和内容写入txt文件
    with open('content.txt', 'a', encoding='utf-8') as file:
        file.write(title + "\n\n")  # 写入标题并换行
        file.write(content_text)    # 写入内容
        file.write("\n\n")

'''
chrome_options = webdriver.ChromeOptions()

# 创建Chrome浏览器实例
driver = webdriver.Chrome(options=chrome_options)

# 打开指定的网页
url = 'https://www.dynxsw.com/book/33730/5607137.html'  # 替换为你要打开的网页
driver.get(url)

# 等待页面加载完成
time.sleep(2)

download(driver)

driver.quit()
'''