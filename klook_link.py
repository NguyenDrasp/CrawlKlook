from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Khởi tạo trình điều khiển (đặt đường dẫn đến ChromeDriver)



driver = webdriver.Edge()

# Mở trang web
driver.get('https://www.klook.com/vi/blog/country/vietnam/?spm=Blog.DestinationLayer&clickId=23333d2d9f')
time.sleep(6)

def getLink(link_list):
    links = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/main/div/div[2]/div[2]/li/a' )
    for link in links:   
        a = link.get_attribute('href') 
        print(a)
        link_list.append(a)
# Thực hiện các thao tác trên trang web
# Ví dụ: Tìm và in nội dung của thẻ h1
link_list = []
getLink(link_list)
next_key = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/main/div/div[2]/div[3]/span[2]/i')

time.sleep(6)

for i in range(0,88):
    next_key[0].click()
    time.sleep(3)
    getLink(link_list)
    next_key = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/main/div/div[2]/div[3]/span[2]/i')


file_path = "links.txt"
# Open the file in write mode
with open(file_path, 'w') as file:
    # Write each element to a new line in the file
    for element in link_list:
        file.write(element + '\n')

# Đóng trình duyệt sau khi hoàn thành
driver.quit()
