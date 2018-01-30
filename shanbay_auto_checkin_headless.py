#coding:utf-8
from selenium import webdriver
from math import ceil
from selenium.webdriver.chrome.options import Options
import time
def strike_card(url):
    driver.get(url)
    time.sleep(1)
    strike_card_btn = driver.find_element_by_xpath("//button[@class='btn btn-large btn-success']")
    strike_card_btn.click()
    print("打卡成功，请注意查收~")
    input("press any key。。。")
    driver.quit()
chrom_options=Options()
chrom_options.add_argument('--headless')
chrom_options.add_argument('--disable-gpu')
driver=webdriver.Chrome(chrome_options=chrom_options)
driver.set_window_size(1920,1080)
try:
    driver.get("https://www.shanbay.com/web/account/login/")
    username_input=input("请输入用户名：")
    password_input=input("请输入密码：")
    username=driver.find_element_by_name("username")
    username.send_keys(username_input)
    password=driver.find_element_by_name("password")
    password.send_keys(password_input)
    form=driver.find_element_by_name("login-form")
    form.submit()
    time.sleep(1)
    driver.refresh()
    time.sleep(1)
    driver.save_screenshot("index.png")
    a_tag=driver.find_elements_by_xpath("//a")
    for i in a_tag:
        if i.text == "首页":
            print(i.get_attribute("href"))
            index = i
        if i.text == "新闻":
            print(i.get_attribute("href"))
            news = i
    index_url = index.get_attribute("href")
    news_url = news.get_attribute("href")
    news.click()
    time.sleep(1)
    if driver.title == "扇贝新闻":
        print("进入新闻界面")
    img_news = driver.find_element_by_xpath("//div[@class='img-news-display']")
    img_news_title = driver.find_element_by_xpath(
        "//div[@class='img-news-display']/descendant::p[@class='img-news-title']")
    print("标题为:%s" % img_news_title.text)
    img_news.click()
    driver.refresh()
    time.sleep(1)
    size_num = driver.find_element_by_xpath('//*[@id="pageContainer"]/div[1]/div/div[1]/span[4]')
    print("字数：%s" % size_num.text)
    sleepy_time = ceil(int(size_num.text) / 8)
    time.sleep(sleepy_time)
    try:
        over = driver.find_element_by_xpath("//a[@class='article-button finish-button']")
        over.click()
    except:
        pass
    driver.get(news_url)
    time.sleep(1)
    ul_news = driver.find_elements_by_xpath("//ul[@class='news']/descendant::a")
    list_url = []
    for i in ul_news:
        list_url.append(i.get_attribute("href"))
    for news in list_url:
        driver.get(news)
        time.sleep(1)
        title = driver.find_element_by_xpath("//*[@id='pageContainer']/div[1]/div/h2")
        print("标题为：%s" % title.text)
        num = title.find_element_by_xpath("//*[@id='pageContainer']/div[1]/div/div[1]/span[4]")
        print("字数：%s" % num.text)
        sleepy_time=ceil(int(num.text)/8)
        time.sleep(sleepy_time)
        try:
            over = driver.find_element_by_xpath("//a[@class='article-button finish-button']")
            over.click()
        except:
            continue
    strike_card(index_url)
except:
    pass
finally:
    driver.quit()