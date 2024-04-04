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
driver.find_element(By.ID,"APjFqb").send_keys("Bukalapak")

#fungsi sleep digunakan untuk membuat delay
time.sleep(6)

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Penelusuran Google)
tombol=driver.find_element(By.CLASS_NAME,"gNO89b")
# tombol2=driver.find_element(By.CLASS_NAME,"LC201b MBeuO DKV0Md")

#jalankan variabel tombol dengan fungsi click()
tombol.click()
# tombol2.click()

# Setelah pencarian, arahkan langsung ke halaman utama Bukalapak
driver.get("https://www.bukalapak.com/")
# menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.ID,"v-omnisearch__input").send_keys("Kacamata")

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Penelusuran Google)
tombol_bukalapak=driver.find_element(By.CLASS_NAME,"ico_search")
#jalankan variabel tombol dengan fungsi click()
tombol_bukalapak.click()