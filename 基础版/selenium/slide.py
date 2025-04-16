import os
import base64
import random
import time

import ddddocr
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver

# 全局初始化 OCR 实例
slide_ocr = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

# 图片配置
IMAGE_CONFIG = {
    "bg": {
        "xpath": '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img',
        "save_path": os.path.join("滑动验证", "背景图.png")
    },
    "slice": {
        "xpath": '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img',
        "save_path": os.path.join("滑动验证", "缺口图.png")
    }
}


def make_img_fetcher(xpath: str):
    """闭包：生成获取图片 URL 的函数"""

    def fetch_func(driver: WebDriver) -> str:
        element = driver.find_element(By.XPATH, xpath)
        return element.get_attribute("src")

    return fetch_func


def get_image_data(
        driver: WebDriver,
        xpath: str,
        save_path: Optional[str] = None
) -> bytes:
    """通用函数：获取并解码图片数据"""
    try:
        fetch_func = make_img_fetcher(xpath)
        img_url = WebDriverWait(driver, 30, 0.5).until(fetch_func)
    except TimeoutException:
        raise RuntimeError(f"图片加载超时，XPath: {xpath}")

    if not img_url.startswith("data:image/"):
        raise ValueError("非图片类型的 Data URL")
    if "," not in img_url:
        raise ValueError("无效的 Base64 格式")

    header, base64_data = img_url.split(",", 1)
    image_data = base64.b64decode(base64_data)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(image_data)
    return image_data


def get_position(driver: WebDriver) -> tuple[int, int, int, int]:
    """计算滑块位置坐标"""
    bg_data = get_image_data(
        driver,
        IMAGE_CONFIG["bg"]["xpath"],
        IMAGE_CONFIG["bg"]["save_path"]
    )
    slice_data = get_image_data(
        driver,
        IMAGE_CONFIG["slice"]["xpath"],
        IMAGE_CONFIG["slice"]["save_path"]
    )

    res = slide_ocr.slide_match(slice_data, bg_data, simple_target=True)
    x1, y1, x2, y2 = res['target']
    print(x1,y1,x2,y2)
    return (x1, y1, x2, y2)


# def generate_human_like_track(distance: int) -> list[tuple[int, int, float]]:
#     """
#     模拟人类滑动轨迹，返回 (x, y, sleep_time) 元组列表
#     """
#     track = []
#     current = 0
#     mid = distance * 3 / 5  # 加速到中点后开始减速
#     t = 0.2
#     v = 0
#
#     while current < distance:
#         if current < mid:
#             a = random.uniform(2.0, 4.0)
#         else:
#             a = -random.uniform(3.0, 5.0)
#
#         v0 = v
#         v = v0 + a * t
#         move = v0 * t + 0.5 * a * t ** 2
#         move = round(move)
#
#         current += move
#         if current > distance:
#             move = distance - (current - move)
#             current = distance
#
#         y_offset = random.randint(-1, 1)
#         sleep_time = random.uniform(0.01, 0.03)
#
#         track.append((move, y_offset, sleep_time))
#
#     # 回弹微调
#     for _ in range(2):
#         track.append((-random.randint(1, 2), 0, random.uniform(0.01, 0.02)))
#         track.append((random.randint(1, 2), 0, random.uniform(0.01, 0.02)))
#
#     return track


# 移动轨迹函数
def get_track8(distance):
    # 移动轨迹
    tracks = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 时间间隔
    t = 0.2
    # 初始速度
    v = 0

    while current < distance:
        if current < mid:
            a = random.uniform(2, 5)
        else:
            a = -(random.uniform(12.5, 13.5))
        v0 = v
        v = v0 + a * t
        x = v0 * t + 1 / 2 * a * t * t
        current += x

        if 0.6 < current - distance < 1:
            x = x - 0.53
            tracks.append(round(x, 2))

        elif 1 < current - distance < 1.5:
            x = x - 1.4
            tracks.append(round(x, 2))
        elif 1.5 < current - distance < 3:
            x = x - 1.8
            tracks.append(round(x, 2))

        else:
            tracks.append(round(x, 2))

    print(sum(tracks))
    return tracks




def move_slide(driver):
    x1, y1, x2, y2 = get_position(driver)

    # 设置目标偏移，防止“完美贴合”
    target_distance = x1+15

    slide_btn = driver.find_element(
        By.XPATH,
        '//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]'
    )

    ActionChains(driver).click_and_hold(slide_btn).perform()

    tracks = get_track8(target_distance)

    for x_offset in tracks:
        ActionChains(driver).move_by_offset(xoffset=x_offset, yoffset=0).perform()
        time.sleep(0.01)

    time.sleep(1)
    ActionChains(driver).release().perform()

