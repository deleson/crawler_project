import time
import random
import slide

from  selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc



# service = Service("driver/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
driver = uc.Chrome()


driver.get('https://passport.jd.com/uc/login?ltype=logout&ReturnUrl=https%3A%2F%2Fitem.jd.com%2F100016518682.html%3Fextension_id%3DeyJhZCI6IiIsImNoIjoiIiwic2hvcCI6IiIsInNrdSI6IiIsInRzIjoiIiwidW5pcWlkIjoie1wiY2xpY2tfaWRcIjpcImNlMTQ5ZWYxLTkxMGYtNDdlMi04N2YzLWMxNjVkODg5ZjA0N1wiLFwicG9zX2lkXCI6XCIyNjE3XCIsXCJzaWRcIjpcIjdlYjJkNDEyLWY5ZTUtNDBhNy1hZWQyLTU3NjYxZGUzNzE1MlwiLFwic2t1X2lkXCI6XCIxMDAwMTY1MTg2ODJcIn0ifQ%3D%3D%26jd_pop%3Dce149ef1-910f-47e2-87f3-c165d889f047')



# 输入用户名
time.sleep(random.uniform(1.3,3.3))
tag_username = driver.find_element(
    By.XPATH,
    '//*[@id="loginname"]'
)
my_username = 'thiskising'
# 一个字符一个字符 send_keys，模拟手动打字
for char in my_username:
    tag_username.send_keys(char)
    time.sleep(random.uniform(0.1, 0.2))  # 模拟人打字的节奏，时间随机更自然



# 输入密码
time.sleep(random.uniform(1.0,2.5))
tag_password = driver.find_element(
    By.XPATH,
    '//*[@id="nloginpwd"]'
)
my_password = '1qaz2wsx3edc'
# 一个字符一个字符 send_keys，模拟手动打字
for char in my_password:
    tag_password.send_keys(char)
    time.sleep(random.uniform(0.1, 0.2))  # 模拟人打字的节奏，时间随机更自然


# 点击登录
time.sleep(random.uniform(1.5,2))
login_btn = driver.find_element(
    By.XPATH,
    '//*[@id="loginsubmit"]'
)
login_btn.click()


time.sleep(3)
# 如果进入滑动验证
slide_check = driver.find_elements(
    By.XPATH,
    '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[1]/div[2]'
)

print(slide_check)
if slide_check:
    print("要开始滑动验证")
    print()
    # print(slide.get_position(driver))
    slide.move_slide(driver)







time.sleep(5000)
driver.close()


