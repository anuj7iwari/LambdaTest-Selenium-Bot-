import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



# Task(1) Opening Lambdatest.com
driver = webdriver.Chrome()

driver.get("https://www.lambdatest.com/")

# TASK(2) Doing explicit wait until all the elements in the DOM are available.

driver.implicitly_wait(10)

# TASK(3) Scrolling until ‘SEE ALL INTEGRATIONS’ comes into view

scroll_into = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/section[7]/div/div/div/div/a')
driver.execute_script("arguments[0].scrollIntoView();", scroll_into)

# TASK(4) Clicking / getting the link of ‘SEE ALL INTEGRATIONS’

see_all_integrations_link = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/section[7]/div/div/div/div/a')

# Considering the link as URL

url = see_all_integrations_link.get_attribute('href')

time.sleep(3)

# TASK(5) Saving handle in a variable and printing the handle

parent_handle = driver.current_window_handle
print("Parent Handle:", parent_handle)

# TASK(5.5) Opening another Tab and link

driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])

driver.get(url)

child_handle = driver.current_window_handle

current_url = driver.current_url

# TASK(6.0) Considering Link as Expected Url

expected_url = url

# TASK(6.5) Assert

assert current_url == expected_url, "The current URL is not the expected one"

time.sleep(3)

# TASK(7) Scrolling to the page where the WebElement (Codeless Automation) is present.

scroll_into_codeless = driver.find_element(By.XPATH, '//*[@id="codeless_row"]/div/div[4]')
driver.execute_script("arguments[0].scrollIntoView();", scroll_into_codeless)

# TASK(8) Clicking the ‘LEARN MORE’ link for Testing Whiz

driver.find_element(By.XPATH, '//*[@id="codeless_row"]/div/div[4]/a').click()

# TASK(9) Verifying whether Title is ''Running Automation Tests Using TestingWhiz LambdaTest | LambdaTest'' or not
# Task is to verify whether Title is ''TestingWhiz LambdaTest | LambdaTest'' or not 
# ("BUT IT SEEMS LIKE TITLE WAS CHANGED TO ''Running Automation Tests Using TestingWhiz LambdaTest | LambdaTest'' ")

expected_title = "Running Automation Tests Using TestingWhiz LambdaTest | LambdaTest"

# Getting the page title

page_title = driver.title

# Assert
assert page_title == expected_title, "This is not the page you are looking for"

# TASK(10) Closing the current tab using window handle

driver.close()

driver.switch_to.window(driver.window_handles[0])

time.sleep(3)

# TASK(11) Counting the tab count

number_of_windows_open = len(driver.window_handles)
print("Number of windows open:", number_of_windows_open)

# TASK(12) Setting ("https://www.lambdatest.com/blog") as the new URL

new_url = "https://www.lambdatest.com/blog"
driver.get(new_url)

# TASK(13) Clicking the community button and verifying the link

community_button = driver.find_element(By.XPATH, '//*[@id="menu-item-10121"]/a') 
community_button.click()

blog_page_url = driver.current_url

expected_url = "https://community.lambdatest.com/"

if blog_page_url == expected_url:
    print("URL Matched To The Given URL")
else:
    print("URL not matched")
    driver.quit()

# TASK(14) Closing the current tab

driver.close()
