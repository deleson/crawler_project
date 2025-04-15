from requests_html import HTMLSession

session = HTMLSession()
url = "https://zhuanlan.zhihu.com/p/376399749"

# 获取响应数据对象
obj = session.get(url)
obj.encoding = 'utf-8'
print(obj.text)

# 1.通过css选择器选取一个Element对象
# 获取id为content-left的div标签，并且返回一个对象
content = obj.html.find('body', first=True)

# 2.获取一个Element对象内的文本内容
# 获取content内所有文本
print(content.text)

# 3.获取一个Element对象的所有attributes
# 获取content内所有属性
print(content.attrs)

# 4.渲染出一个Element对象的完整的HTML内容
html = content.html
print(html)

# 5.获取Element对象内的指定的所有子Element对象，返回列表
a_s = content.find('script')
print(a_s)
print(len(a_s))  # 79

# 循环所有的a标签
for a in a_s:
    # 获取a标签内所有属性的href属性 并拼接
    href = a.attrs['src']
    if href.startswith('/'):
        url = 'https://zhuanlan.zhihu.com/p/376399749' + href
        print(url)
    else:
        print(href)

# 6.在获取的页面中通过search查找文本
# {}大括号相当于正则的从头到后开始匹配，获取当中想要获取的数据
text = obj.html.search('知乎{}世界')[0]  # 获取从 "把" 到 "夹" 字的所有内容
text = obj.html.search('让每一次{}意义')[0]
print(text)

print('*' * 1000)

# 7.支持XPath
a_s = obj.html.xpath('//a')  # 获取html内所有的a标签
for a in a_s:
    href = a.attrs['href']

    # 若是//开头的url都扔掉
    if href.startswith('//'):
        continue

    # 若是/开头的都是相对路径
    elif href.startswith('/'):
        print('https://www.qiushibaike.com' + href)


# 8.获取到只包含某些文本的Element对象（containing）
# 获取所有文本内容为幽默笑话大全_爆笑笑话_笑破你的肚子的搞笑段子 - 糗事百科 title标签
# 注意: 文本内有空格也必须把空格带上
title = obj.html.find('title', containing='幽默笑话大全_爆笑笑话_笑破你的肚子的搞笑段子 - 糗事百科')
print(title)