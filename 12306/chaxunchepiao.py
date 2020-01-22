from winsound import Beep

from selenium import webdriver
import time
# 专业处理下拉框元素
from selenium.webdriver.support.select import Select

path = r"C:\Users\36948\Desktop\jing2019-1-7\12306\chromedriver.exe"
url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"

# 返回一个对象 browser就是我们的一个浏览器
browser = webdriver.Chrome(path)

time.sleep(5)
browser.get(url)

# 元素定位
# 出发地id fromStationText
start_city = browser.find_element_by_id("fromStationText")
# 元素交互 click() 模拟鼠标单击事件
start_city.click()
# clear() 清空内容
start_city.clear()
# send_keys(输入内容)
start_city.send_keys("西安\n")

# 目的地id： toStationText
end_city = browser.find_element_by_id("toStationText")
# 元素交互 click() 模拟鼠标单击事件
end_city.click()
# clear() 清空内容
end_city.clear()
# send_keys(输入内容)
end_city.send_keys("广州\n")

choice_time = Select(browser.find_element_by_id("cc_start_time"))
# choice_time.select_by_index()
choice_time.select_by_visible_text("00:00--24:00")

data = browser.find_element_by_css_selector("#date_range li:nth-child(1)")
data.click()

# 防止有网络延迟
time.sleep(5)

favorite = ["G3", "G137", "G21"]

xpath = '//tbody[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'
train_list = browser.find_elements_by_xpath(xpath)

for train in train_list:
    train_num = train.text
    if train_num in favorite:
        print("亲  有票了哦！！！")
        target = train.find_elements_by_xpath('../../../../../td[13]/a')[0]
        # print(target)
        target.click()
        input("请手动登陆  登陆成功之后请按回车键")

        time.sleep(3)
        browser.find_element_by_id("normalPassenger_0").click()
        browser.find_element_by_id("submitOrder_id").click()

        time.sleep(10)
        browser.find_element_by_id("qr_submit_id").click()

        print("亲  恭喜您抢票成功!!!")
        # 第一个参数代表声音大小  第二个参数代表时长  1000 = 1秒
        Beep(3000, 3000)
        break
    else:
        print("亲  暂时还没有票  请耐心等待...")
browser.quit()
