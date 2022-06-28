"""
内存泄露

创建了对象使用后，但是并没有正确释放或其他问题导致遗留在内存中

"""


class Demo:

    class_name = ''


a1 = Demo()
a2 = Demo()
a1.child = a2
a2.child = a1

"""
循环引用 导致到内存泄露 主要是引用计数无法清0
"""
from selenium import webdriver


webdriver_client = webdriver.Chrome()
webdriver_client.get("www.baidu.com")
webdriver_client.close()
# webdriver_client.quit()


"""
没有正常关闭导致的Chrome webdriver进程依然在
"""
