from selenium import webdriver
# menggunakan fungsi By
from selenium.webdriver.common.by import By
# menggunakan fungsi time
import time

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=options)

driver.get("https://google.com/")
# menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.ID,"APjFqb").send_keys("demo guru99")

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Penelusuran Google)
tombol=driver.find_element(By.CLASS_NAME,"gNO89b")

#jalankan variabel tombol dengan fungsi click()
tombol.click()

#fungsi sleep digunakan untuk membuat delay
time.sleep(3)

# Setelah pencarian, arahkan langsung ke halaman utama Bank
driver.get("https://demo.guru99.com/V4/")

# menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.NAME,"uid").send_keys("mngr564473")

#fungsi sleep digunakan untuk membuat delay
time.sleep(3)

# menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.NAME,"password").send_keys("vahenut")

#fungsi sleep digunakan untuk membuat delay
time.sleep(3)

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Login)
buttonLogin=driver.find_element(By.NAME,"btnLogin")

#jalankan variabel tombol dengan fungsi click()
buttonLogin.click()

time.sleep(7)

option_new_customer = driver.find_element(By.XPATH, "//html/body/div[3]/div/ul/li[2]/a")
option_new_customer.click()

time.sleep(7)

# Find the input field by XPath
input_field = driver.find_element(By.XPATH, "//html/body/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input")

# Input the text
input_field.send_keys("Daffa Audya")

#fungsi sleep digunakan untuk membuat delay
time.sleep(2)

# Find the input field by XPath
input_field_dob = driver.find_element(By.XPATH, "//html/body/table/tbody/tr/td/table/tbody/tr[6]/td[2]/input")

# Input the text
input_field_dob.send_keys("06/14/2000")

#fungsi sleep digunakan untuk membuat delay
time.sleep(2)

driver.find_element(By.NAME,"addr").send_keys("Sarijadi")

#fungsi sleep digunakan untuk membuat delay
time.sleep(1)

driver.find_element(By.NAME,"city").send_keys("Bandung")
time.sleep(1)
driver.find_element(By.NAME,"state").send_keys("West Java")
time.sleep(1)
driver.find_element(By.NAME,"pinno").send_keys("405591")
time.sleep(1)
driver.find_element(By.NAME,"telephoneno").send_keys("0821177719876")
time.sleep(1)
driver.find_element(By.NAME,"emailid").send_keys("dapskuys@gmail.com")
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys("dapsdaps")
time.sleep(1)
buttonSubmitNew=driver.find_element(By.NAME,"sub")
buttonSubmitNew.click()
time.sleep(10)