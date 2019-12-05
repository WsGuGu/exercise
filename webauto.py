"""
自动到虎扑网站
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe')
wd.implicitly_wait(10)
wd.get('https://www.baidu.com')
wd.find_element_by_css_selector('#kw').send_keys('虎扑')
wd.find_element_by_css_selector('#su').click()
wd.find_element_by_xpath("//div[@id='1']/h3/a[@data-click]").click()
own = wd.current_window_handle
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if wd.title == '虎扑':
        break
wd.find_element_by_xpath("//div[@class='item-col item-col1']/b/a").click()
act = ActionChains(wd)
act.move_to_element(wd.find_element_by_xpath('//a[@data-nav="论坛"][@class="menu-floor-list-link "]')).perform()
wd.find_element_by_xpath('//a[@data-title=" 话题区"]').click()
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if '足球话题区' in wd.title:
        break