from requests_html import HTMLSession

# 获取请求对象
session = HTMLSession()

# 往京东主页发送get请求
jd = session.get('https://jd.com/')

# 得到京东主页所有的链接，返回的是一个set集合
print(jd.html.links)
print('*' * 1000)

# 若获取的链接中有相对路径，我们还可以通过absolute_links获取所有绝对链接
print(jd.html.absolute_links)