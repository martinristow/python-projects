from selenium import webdriver
from selenium.webdriver.common.by import By
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
driver.get("https://www.python.org/")

#Selenium is better than BeautifulSoup because we cut a lot of code
#in writing and with Selenium we look like a real person doing the same things
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)  # Return tag name in this case will return input
print(search_bar.get_attribute("placeholder")) # This function will return text in placeholder from input

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

help_general_contact_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[1]/a')
print(help_general_contact_link.text)

# driver.close()  # close() will close that particular tab
driver.quit()  # quit() will actually quit the entire program
