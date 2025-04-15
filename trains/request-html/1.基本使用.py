from requests_html import HTMLSession

# 获取请求对象
session = HTMLSession()

# 往新浪新闻主页发送get请求
sina = session.get('https://pypi.org/project/requests-html/')
# print(sina.status_code)
sina.encoding = 'utf-8'

# 获取响应文本信息，与requests无区别
print(sina.text)
