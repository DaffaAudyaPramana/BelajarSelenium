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
driver.find_element(By.ID,"APjFqb").send_keys("Shopee")

#fungsi sleep digunakan untuk membuat delay
time.sleep(3)

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Penelusuran Google)
tombol=driver.find_element(By.CLASS_NAME,"gNO89b")
# tombol2=driver.find_element(By.CLASS_NAME,"LC201b MBeuO DKV0Md")

#jalankan variabel tombol dengan fungsi click()
tombol.click()
# tombol2.click()

# Setelah pencarian, arahkan langsung ke halaman utama Shopee
driver.get("https://www.shopee.co.id/")

# menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.NAME,"loginKey").send_keys("Helm Cakil")

# menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input").send_keys("Helm Cakil")

# menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.CLASS_NAME,"shopee-searchbar-input__input").send_keys("Helm Cakil")

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Penelusuran Google)
tombol_shopee=driver.find_element(By.CLASS_NAME,"btn btn-solid-primary btn--s btn--inline shopee-searchbar__search-button")
#jalankan variabel tombol dengan fungsi click()
tombol_shopee.click()