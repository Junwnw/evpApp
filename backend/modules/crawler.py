# modules/crawler.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def get_weibo_hot(keyword=""):
    try:
        # 配置无头浏览器
        options = Options()
        options.add_argument("--headless")  # 无界面
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("user-agent=Mozilla/5.0")  # 添加 UA 伪装

        # 启动浏览器
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://s.weibo.com/top/summary")

        # 等待 table 加载完成（最长 10 秒）
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        html = driver.page_source
        driver.quit()

        # 解析 HTML
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table")
        if not table:
            return [{"error": "未找到热搜表格"}]

        results = []
        for row in table.find_all("tr")[1:]:  # 跳过标题行
            cols = row.find_all("td")
            if len(cols) >= 2:
                title = cols[1].get_text(strip=True)
                if not keyword or keyword in title:
                    results.append({"title": title})

        return results

    except Exception as e:
        return [{"error": f"抓取失败：{str(e)}"}]


def crawl(data):
    from flask import jsonify
    keyword = data.get("keyword", "").strip()
    result = get_weibo_hot(keyword)
    return jsonify(result)
