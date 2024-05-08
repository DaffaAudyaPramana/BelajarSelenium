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
driver.find_element(By.ID,"APjFqb").send_keys("instagram")

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Penelusuran Google)
tombol=driver.find_element(By.CLASS_NAME,"gNO89b")

#jalankan variabel tombol dengan fungsi click()
tombol.click()

#fungsi sleep digunakan untuk membuat delay
time.sleep(6)

# Setelah pencarian, arahkan langsung ke halaman utama instagram
to_instagram = driver.find_element(By.XPATH, "//html/body/div[4]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/table/tbody/tr[3]/td/div/div/div/div/h3/a")
to_instagram.click()

#fungsi sleep digunakan untuk membuat delay
time.sleep(8)

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button menuju sign up instagram)
option_signup = driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[2]/span/p/a/span")
option_signup.click()

#fungsi sleep digunakan untuk membuat delay
time.sleep(2)

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button menuju kolom no hp atau email)
email_input = driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input")
email_input.send_keys("tempatwisata2023@gmail.com")

#fungsi sleep digunakan untuk membuat delay
time.sleep(2)

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button menuju kolom full name)
full_name_input = driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input")
full_name_input.send_keys("Wegotour")

#fungsi sleep digunakan untuk membuat delay
time.sleep(2)

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button menuju kolom username instagram)
username_input = driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input")
username_input.send_keys("Wegotour81497")

#fungsi sleep digunakan untuk membuat delay
time.sleep(2)

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button menuju kolom password instagram)
password_input = driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/label/input")
password_input.send_keys("ayokitapastibisa123!")

#fungsi sleep digunakan untuk membuat delay
time.sleep(3)

#buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button menuju sign up instagram)
signup_button = driver.find_element(By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[8]/div")
signup_button.click()