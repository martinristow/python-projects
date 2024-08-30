from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".js-start-test .start-text")
        go_button.click()
        time.sleep(50)
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".result-data .download-speed").text
        print(f"down: {self.down}")
        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".result-data .upload-speed").text
        print(f"up: {self.up}")

    def tweet_at_provider(self, twitter_path, twitter_email, twitter_username, twitter_password, promised_down, promised_up):
        self.driver.get(url=twitter_path)
        sing_in_button = self.driver.find_element(By.CSS_SELECTOR,
                                                  value='#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010 > main > div > div > div.css-175oi2r.r-tv6buo.r-791edh.r-1euycsn > div.css-175oi2r.r-1777fci.r-nsbfu8.r-1qmwkkh > div > div.css-175oi2r > div.css-175oi2r.r-2o02ov > a > div')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", sing_in_button)
        time.sleep(3)
        sing_in_button.click()

        time.sleep(5)
        email_input = self.driver.find_element(By.CSS_SELECTOR, value='#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div > div > div.css-175oi2r.r-1mmae3n.r-1e084wi.r-13qz1uu > label')
        email_input.send_keys(twitter_email)

        next_button = self.driver.find_element(By.CSS_SELECTOR, value='#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div > div > button:nth-child(6) > div')
        next_button.click()
        time.sleep(5)

        username_input = self.driver.find_element(By.CSS_SELECTOR, value='#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-175oi2r.r-1mmae3n.r-1e084wi > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-is05cd.r-ttdzmv > div > input')
        username_input.send_keys(twitter_username)
        time.sleep(4)

        button_next = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div')
        button_next.click()
        time.sleep(3)


        password_input = self.driver.find_element(By.CSS_SELECTOR, value='#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-175oi2r.r-1e084wi.r-13qz1uu > div > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-is05cd.r-ttdzmv > div.css-146c3p1.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-135wba7.r-16dba41.r-1awozwy.r-6koalj.r-1inkyih.r-13qz1uu > input')
        password_input.send_keys(twitter_password)
        time.sleep(2)

        log_in_button = self.driver.find_element(By.CSS_SELECTOR, value='#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-1f0wa7y > div > div.css-175oi2r > div > div > button > div')
        log_in_button.click()
        time.sleep(14)

        tweet_message = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when i pay for {promised_down}down/{promised_up}up?"
        tweet_input = self.driver.find_element(By.CSS_SELECTOR, value='#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div.css-175oi2r.r-kemksi.r-1kqtdi0.r-1ua6aaf.r-th6na.r-1phboty.r-16y2uox.r-184en5c.r-1c4cdxw.r-1t251xo.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > div > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')
        tweet_input.send_keys(tweet_message)
        time.sleep(5)

        # Find and click the "Tweet" button to post the Internet Download And Upload Speed
        post_button = self.driver.find_element(By.CSS_SELECTOR, value='#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div.css-175oi2r.r-kemksi.r-1kqtdi0.r-1ua6aaf.r-th6na.r-1phboty.r-16y2uox.r-184en5c.r-1c4cdxw.r-1t251xo.r-f8sm7e.r-13qz1uu.r-1ye8kvj > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-175oi2r.r-kemksi.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > button > div > span > span')
        post_button.click()
