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

option_new_customer = driver.find_element(By.XPATH, "//html/body/div[3]/div/ul/li[5]/a")
option_new_customer.click()

time.sleep(2)

# # menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.NAME,"cusid").send_keys("79172")

# #fungsi sleep digunakan untuk membuat delay
time.sleep(2)

# # menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.NAME,"inideposit").send_keys("200000")

# #fungsi sleep digunakan untuk membuat delay
time.sleep(2)

# #buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Login)
buttonsubmit=driver.find_element(By.NAME,"button2")

# #jalankan variabel tombol dengan fungsi click()
buttonsubmit.click()

time.sleep(15)