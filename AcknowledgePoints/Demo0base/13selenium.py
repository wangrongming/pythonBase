#自动化测试库 驱动浏览器 解决JavaScript渲染问题
#
# pip install selenium

#声明浏览器对象
from selenium import webdriver
browser = webdriver.Chrome()
browser = webdriver.PhantomJS()
#访问页面
browser.get('http://www.baidu.com')
print(browser.page_source)
browser.close()
#查找单个元素
browser.find_element_by_xpath('//*[@id="q"]')
browser.find_element_by_css_selector('#q')
browser.find_element_by_id('q')
browser.find_element_by_link_text()
browser.find_element_by_name()
browser.find_element_by_tag_name()
browser.find_element_by_class_name()
#查找多个元素 返回列表
    #element 变为 elements


#元素交互操作
from selenium import webdriver
import time
input = browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('ipad')
button = browser.find_element_by_class_name('btn-serach')
button.click()

#元素拖拽
from selenium.webdriver import ActionChains
browser.get(url)
browser.switch_to.frame('iframe')
source = browser.find_element_by_css_selector('#drag')
target = browser.find_element_by_css_selector('#grop')
action = ActionChains(browser)
action.drag_and_drop(source,target)
action.perform()

#执行javascript操作
browser.execute_script('alert("To Bottom")')
browser.execute_script('进度条下拉')

#获取元素信息
logo = browser.find_element_by_id()
logo.get_attribute('class')#获取属性
logo.text#获取文本值
logo.id
logo.location
logo.tag_name
logo.size

#Frame
from selenium.common.exceptions import NoSuchElementException
browser.switch_to.frame('child')
browser.switch_to.parent_frame()

#等待
    #隐式等待
    browser.implicitly_wait(10)
    browser.get('http://www.baidu.com')
    #显式等待
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    browser.get('https://www.taobao.com')
    wait = WebDriverWait(browser,10)
    input = wait.until(EC.presence_of_element_located(By.ID,'q'))
    button = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR,'.bin'))
    #selenium-python.readthedocs.io

    #前进后退
    browser.back()
    browser.forward()

    #cookie
    browser.get_cookies()
    browser.add_cookie()
    browser.delete_all_cookies()

#管理网页的选项卡
    browser.execute_script('window.open()')#最通用的方式
    browser.switch_to.window(browser.window_handles[1])#切换到第二个选项卡
#异常处理

