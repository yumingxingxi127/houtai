#!/user/bin/python
#  -*-coding: utf-8-*-
import unittest
import time
from selenium.webdriver.common.by import By
from appium import webdriver
import time
import sys
import iselementexist

import MySQLdb

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


def query_database(self, sql):
    # coon = MySQLdb.connect(host='cpaytest.tinywan.com', user='root', passwd='123456', db='cpay', port=3306,
    #                        charset='utf8')
    coon = MySQLdb.connect(host='cpay.hypayde.com', user='root', passwd='root123456', db='cl_cpay', port=3306,
                           charset='utf8')
    # cursor = coon.cursor()
    cursor = coon.cursor(cursorclass=MySQLdb.cursors.DictCursor)  # 带有键值对的数组
    try:
        cur = cursor.execute(sql)
        rows = cursor.fetchall()
        qrcode_url = []
        # print rows
        for row in rows:
            # print row["qrcode_url"]
            qrcode_url.append(row["qrcode_url"])
        # print rows
        return qrcode_url
    except:
        print "Error: This is except"
        # coon.commit()
    coon.close()



class zhifubao(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfromVersion'] = '7.1.1'
        desired_caps['deviceName'] = '33d04c7c'
        desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
        desired_caps['automationName'] = 'uiautomator2'  ##############
        desired_caps['appActivity'] = 'com.eg.android.AlipayGphone.AlipayLogin'
        desired_caps['noReset']=True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_zhifubao(self):
        driver=self.driver
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='朋友']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.TextView[@text='温州赤龙网络科技有限公司']").click()
        time.sleep(1)
        # f0 = open('D:\\zxtest\\cpay.txt', 'r')#备注
        # z = len(open('D:\\zxtest\\cpay.txt', 'r').readlines())
        # f1=open('D:\\zxtest\\zhifubao.txt', 'r')#二维码
        # f1=open('D:\\zxtest\\cpayzhifubao.txt', 'r')#二维码
        sql = "SELECT qrcode_url FROM `cl_merchant_qrcode`where mch_id=1006 and expire_time>0 "
        # sql="update cl_merchant_qrcode set expire_time=0 where mch_id=1006 and expire_time>0"
        erweimas =query_database(self,sql)


        for erweima in erweimas:
            # beizhu = f0.readline()
            # erweima=f1.readline()

            print "erweima:%s"%erweima
            if erweima == '':
                break
            time.sleep(2)
            driver.find_element_by_xpath("//android.widget.EditText[@index='0']").send_keys(erweima)
            time.sleep(4)
            driver.find_element_by_xpath("//android.widget.TextView[@text='发送']").click()
            time.sleep(2)
            lianjies=driver.find_elements_by_id("com.alipay.mobile.chatapp:id/chat_msg_text")
            print type(lianjies)
            # print lianjies
            time.sleep(2)
            lianjies[-1].click()
            time.sleep(5)
            element01="//android.widget.Button[@text='确认转账']"
            if iselementexist.isElementExist(self,element01):
                pass
            else:
                lianjies[-1].click()
                time.sleep(2)
            driver.implicitly_wait(100)
            driver.find_element_by_id("com.alipay.mobile.payee:id/payee_NextBtn").click()
            time.sleep(5)
            driver.find_element_by_xpath("//android.widget.TextView[@text='立即付款']").click()
            # driver.find_element_by_android_uiautomator('new UiSelector().text("立即付款")')

            time.sleep(1)
            x=driver.get_window_size()['width']
            y=driver.get_window_size()['height']
            driver.tap([(140*x/1080,1500*y/1920)],0)
            driver.tap([(200*x/1080,1500*y/1920)],0)
            driver.tap([(800*x/1080,1500*y/1920)],0)
            driver.tap([(800*x/1080,1500*y/1920)],0)
            driver.tap([(500*x/1080,1680*y/1920)],0)
            driver.tap([(500*x/1080,1680*y/1920)],0)
            time.sleep(3)

            element="//android.widget.TextView[@text='开通指纹支付']"
            if iselementexist.isElementExist(self,element):
                driver.find_element_by_xpath("//android.widget.TextView[@text='取消']").click()
                time.sleep(3)
            else:
                pass
            time.sleep(2)
            driver.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()
            time.sleep(1)


        # f1.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()