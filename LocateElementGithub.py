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
driver.find_element(By.ID,"APjFqb").send_keys("Techpowerup")

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Penelusuran Google)
tombol=driver.find_element(By.CLASS_NAME,"gNO89b")

#jalankan variabel tombol dengan fungsi click()
tombol.click()

#fungsi sleep digunakan untuk membuat delay
time.sleep(3)

# Setelah pencarian, arahkan langsung ke halaman utama Techpowerup
driver.get("https://www.techpowerup.com/")
# menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.NAME,"search1").send_keys("Nvidia Driver")

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Penelusuran Google)
tombol_tech=driver.find_element(By.CLASS_NAME,"s--search__submit")
#jalankan variabel tombol dengan fungsi click()
tombol_tech.click()