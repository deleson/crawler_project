from requests_html import HTMLSession
import os
os.environ["PYPPETEER_EXECUTABLE_PATH"] = "C:\Program Files\Google\Chrome\Application\chrome.exe"
session = HTMLSession()
url = "https://pypi.org/project/requests-html/"

# 渲染页面（执行 JavaScript）
response = session.get(url)
response.html.render()  # 等待 JS 执行

# 获取渲染后的 HTML
print(response.html.html)