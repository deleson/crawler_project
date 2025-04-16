京东的反爬机制中等偏强，虽然不像淘宝那样全 JS 渲染 + 滑块验证那样激进，但也有不少细节值得注意。下面是你作为个人开发者在抓取京东数据时**必须了解的几个核心反爬点**，以及**绕过方法建议**：

------

### 🛡️ 京东常见反爬机制

| 机制类型                         | 说明                           | 应对建议                                     |
| -------------------------------- | ------------------------------ | -------------------------------------------- |
| 1. **User-Agent 验证**           | 默认 Python UA 会被拦          | 使用 `fake_useragent` 随机化                 |
| 2. **Referer 检查**              | 检查请求是否从京东内页跳转     | 添加合理 Referer，例如 `https://www.jd.com`  |
| 3. **Cookie 校验**               | 某些接口需带 Cookie 才返回数据 | 可用 Selenium 抓 Cookie 预填充               |
| 4. **频率限制/IP封禁**           | 同一IP频繁请求触发风控         | 添加代理池 + 随机延迟                        |
| 5. **动态加载（JS渲染）**        | 商品详情页价格、评价是动态加载 | 需要 `render()` 或模拟 Ajax 请求             |
| 6. **UA + Fingerprint 联合检测** | 针对浏览器指纹识别（严重时）   | 非常频繁采集时才触发，建议模拟行为、人机混合 |

------

### 🧪 实战抓取前准备

#### ✅ 选择合适页面

建议从**搜索结果页**或**商品详情页 URL**入手，不走 Ajax 接口路径，避免额外加密分析。

示例商品页：

```
https://item.jd.com/100020211266.html
```

------

### 🛠️ 最小反爬规避示例（Requests-HTML）

```python
from requests_html import HTMLSession
import fake_useragent
import time, random

session = HTMLSession()

def get_jd_page(url):
    headers = {
        'User-Agent': fake_useragent.UserAgent().random,
        'Referer': 'https://www.jd.com',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    try:
        r = session.get(url, headers=headers, timeout=10)
        r.html.render(sleep=random.uniform(1, 2), scrolldown=1)
        return r.html
    except Exception as e:
        print(f"抓取失败: {e}")
        return None
```

------

### 🧩 其他反爬小技巧

- **模拟人工等待**：不要使用 `time.sleep(5)`，使用 `np.random.normal()` 生成延迟。
- **滚动加载支持**：很多商品页面的评论、推荐模块是通过滚动触发的，记得添加 `scrolldown=n`。
- **识别是否被反爬**：返回页面为京东首页、空页面、登录页、JSON 包含 `"error":"overload"`，都意味着触发了反爬。

------

### 📌 开发建议流程

1. 用浏览器访问目标页面，F12 → 查看加载逻辑（是否有 JS 异步）
2. 写 `Requests-HTML` 抓取脚本 + `render()` 测试数据
3. 添加 User-Agent / Referer / 随机 delay
4. 如果连续请求失败，加入 Cookie 或切换代理（免费代理命中率低，建议预设）

------

想不想我帮你写一个抓取京东某个商品价格和标题的 demo？你贴个商品链接或者类目页，我来写抓取逻辑。







# 1.滑块验证频繁

```python
import undetected_chromedriver as uc

driver = uc.Chrome()
```

简单的这个不能有效减少滑块验证的频率。





# 2.滑动验证不通过

使用selenium模拟的轨迹，即使完美贴合也不能通过滑块验证。