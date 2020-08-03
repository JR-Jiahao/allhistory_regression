# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException


class IsElemnetExist:
    """
    通过id来定位判断某个元素是否存在
    """
    @classmethod
    def is_element_exist_byid(cls, driver, element):
        try:
            driver.find_element_by_id(element)
            return True
        except NoSuchElementException:
            return False

    """
    通过id来定位获取某个元素对应的文本信息
    """
    @classmethod
    def is_text_right_byid(cls, driver, element):
        try:
            text = driver.find_element_by_id(element).text
            return text
        except NoSuchElementException:
            return False

    """
    当没有id但是有多个class时，通过css selector来定位获取元素对应的文本信息
    """
    @classmethod
    def is_text_right_by_css_selector(cls, driver, element):
        try:
            text = driver.find_element_by_css_selector(element).text
            return text
        except NoSuchElementException:
            return False

    """
    当没有id也没有合适的class时，通过xpath来定位获取元素对应的文本信息
    """
    @classmethod
    def is_text_right_by_xpath(cls, driver, element):
        try:
            text = driver.find_element_by_xpath(element).text
            return text
        except NoSuchElementException:
            return False

    """
    当没有id也没有合适的class时，通过xpath来定位元素并触发点击事件
    """
    @classmethod
    def click_by_xpath(cls, driver, element):
        try:
            driver.find_element_by_xpath(element).click()
            return True
        except NoSuchElementException:
            return False
