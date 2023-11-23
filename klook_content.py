from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()
# Đường dẫn của tệp văn bản chứa các phần tử (thay đổi thành đường dẫn thực tế của bạn)
file_path = "links.txt"

# Mở tệp văn bản để đọc
with open(file_path, 'r') as file:
    # Đọc nội dung của tệp và chia thành các dòng
    lines = file.readlines()

# Xóa khoảng trắng và ký tự xuống dòng từ mỗi dòng và tạo danh sách các phần tử
elements = [line.strip() for line in lines]
i = 0
# In danh sách các phần tử
for element in elements[:3]:
    driver.get(element)
    time.sleep(6)
    head = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div[1]/div[1]/h1').text
    print(head)
    
    file_path = "content"+ str(i) +'.txt'
    # Open the file in write mode
    with open(file_path, 'w', encoding='utf-8') as file:
        # Write each element to a new line in the file
        file.write(head)
    i = i+1