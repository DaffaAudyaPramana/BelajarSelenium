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
driver.find_element(By.ID,"APjFqb").send_keys("Netflix")

#fungsi sleep digunakan untuk membuat delay
time.sleep(6)

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Penelusuran Google)
tombol=driver.find_element(By.CLASS_NAME,"gNO89b")
# tombol2=driver.find_element(By.CLASS_NAME,"LC201b MBeuO DKV0Md")

#jalankan variabel tombol dengan fungsi click()
tombol.click()
# tombol2.click()

# Setelah pencarian, arahkan langsung ke halaman utama Netflix
driver.get("https://www.netflix.com/")
# menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.ID,":r0:").send_keys("Netflix@gmail.com")

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Penelusuran Google)
tombol_netflix=driver.find_element(By.CLASS_NAME,"default-ltr-cache-17uj5h e1ax5wel0")
#jalankan variabel tombol dengan fungsi click()
tombol_netflix.click()