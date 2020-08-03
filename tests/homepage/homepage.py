# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/26 14:32
@Author  : JR
@FileName: homepage.py
@Software: PyCharm
"""
import pytest
import datetime
from appium import webdriver
from Base.app_config import caps
from is_element_exist import IsElemnetExist
driver = webdriver.Remote("http://localhost:4725/wd/hub", caps)


def teardown_module():
    driver.quit()


def test_1_top_head():
    """
    测试要点
    1.全历史图标
    2.显示搜索框
    3.日期显示
    4.搜索框默认文本
    5.点击顶部搜索框进入搜索激活页
    """
    el1 = driver.find_element_by_id("com.allhistory.dls.marble:id/tv_close")
    el1.click()
    """
    1. 检查是否显示全历史图标
    """
    if IsElemnetExist.is_element_exist_byid(driver, "com.allhistory.dls.marble:id/icon") is True:
        print("全历史图标显示正确")
    else:
        print("全历史图标不存在")
    """
    2. 检查是否显示搜索框
    """
    if IsElemnetExist.is_element_exist_byid(driver, "com.allhistory.dls.marble:id/searchArea") is True:
        print("搜索框已显示")
    else:
        print("搜索框未显示")
    """
    3.检查日期信息是否显示且日期是否正确
    先定义一个字典，从0-6，对应周一到周日
    """
    week_day_dict = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周天',
    }
    """
    获取当日的时间
    """
    today = datetime.datetime.now()
    """
    调用weekday()函数
    Return the day of the week as an integer, where Monday is 0 and
    Sunday is 6.
    :rtype: int
    """
    week_day = today.weekday()
    """
    格式化获取的今日日期只精确到月，例:格式化为:2020.07
    """
    today.strftime('%Y.%m')
    print(today.strftime('%d'))
    """
    因为top head的日期格式为:
    周二
    2020.07
    所以，将week_day_dict[week_day]获取今日是周几，和格式化后的日期(2020.07)进行字符串拼接，中间加上回车转义符。
    这样格式就和top head的日期格式保持一致了
    """
    date_of_today = str(week_day_dict[week_day]) + '\n' + str(today.strftime('%Y.%m'))
    print(str(week_day_dict[week_day]) + '\n' + str(today.strftime('%Y.%m')))
    """
    获取top head的日期,年月
    """
    date_on_top_head = IsElemnetExist.is_text_right_byid(driver, "com.allhistory.dls.marble:id/tv_week_year_month")
    """
    获取top head的日期,日
    """
    day_on_top_head = IsElemnetExist.is_text_right_byid(driver, "com.allhistory.dls.marble:id/tv_date")
    print(IsElemnetExist.is_text_right_byid(driver, "com.allhistory.dls.marble:id/tv_week_year_month"))
    """
    将获取的top head日期与当前的今日日期做对比
    """
    if date_of_today == date_on_top_head and today.strftime('%d') == day_on_top_head:
        print("日期信息已显示且日期正确")
    else:
        print("日期信息未显示或者日期不正确")
    """
    4.检查搜索框默认文本是否正确
    """
    search_text = IsElemnetExist.is_text_right_by_xpath(driver, "/hierarchy/android.widget.FrameLayout/"
                                                                "android.widget.LinearLayout/"
                                                                "android.widget.FrameLayout/"
                                                                "android.widget.LinearLayout/"
                                                                "android.widget.FrameLayout/"
                                                                "android.view.ViewGroup/"
                                                                "android.widget.FrameLayout[2]/"
                                                                "android.view.ViewGroup/"
                                                                "android.widget.TextSwitcher/"
                                                                "android.widget.TextView")
    print(search_text)
    if search_text == "搜索全历史":
        print("搜索框默认文本显示正确")
    else:
        print("搜索框文本显示不正确")
    """
    5.点击顶部搜索框进入搜索激活页
    """
    driver.find_element_by_id("com.allhistory.dls.marble:id/img_magnifier").click()

    if IsElemnetExist.is_element_exist_byid(driver, "com.allhistory.dls.marble:id/historyFragment") is True:
        print("进入搜索激活页成功")
        driver.find_element_by_id("com.allhistory.dls.marble:id/tv_cancel").click()
    else:
        print("进入搜索激活页失败")


def test_2_homepage_guide():
    """
    首页导览
    所有模块导览入口；第一行固定5个模块
    1.Top 100 2.时空地图 3.关系图谱 4.AB路径 5.全规律
    """
    linear_layout = 5
    i = 1
    while i <= linear_layout:
        guide_dict = {
            1: "Top100",
            2: "时空地图",
            3: "关系图谱",
            4: "AB路径",
            5: "全规律"
        }
        if IsElemnetExist.click_by_xpath(driver, "/hierarchy/android.widget.FrameLayout/"
                                                 "android.widget.LinearLayout/"
                                                 "android.widget.FrameLayout/"
                                                 "android.widget.LinearLayout/"
                                                 "android.widget.FrameLayout/"
                                                 "android.view.ViewGroup/"
                                                 "android.widget.FrameLayout[2]/"
                                                 "android.view.ViewGroup/"
                                                 "android.widget.FrameLayout[2]/"
                                                 "android.view.ViewGroup/"
                                                 "androidx.recyclerview.widget.RecyclerView/"
                                                 "android.widget.FrameLayout[1]/"
                                                 "android.widget.LinearLayout/"
                                                 "androidx.recyclerview.widget.RecyclerView[1]/"
                                                 "android.widget.LinearLayout" + str([i]) + "/"
                                                 "android.widget.ImageView") is True:

            print(guide_dict[i]+" PASS")
            if i == 2:
                driver.find_element_by_id("com.allhistory.dls.marble:id/img_close").click()
            else:
                driver.find_element_by_id("com.allhistory.dls.marble:id/img_topbar_left").click()
            i += 1
        else:
            print(guide_dict[i]+" FAILED")
            break


if __name__ == "__main__":
    pytest.main(['homepage.py'])
    #test_1_top_head()
    #test_2_homepage_guide()
