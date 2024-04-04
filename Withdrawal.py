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

# Setelah daftar untuk pelanggan baru, arahkan langsung ke halaman membuat akun bank baru
driver.get("https://demo.guru99.com/V4/manager/WithdrawalInput.php")

# # menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.NAME,"accountno").send_keys("133527")

# #fungsi sleep digunakan untuk membuat delay
time.sleep(2)

# # menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.NAME,"ammount").send_keys("50000")

# #fungsi sleep digunakan untuk membuat delay
time.sleep(2)

# # menggunakan fungsi By untuk mengetahui element di web menggunakan ID dan keyword
driver.find_element(By.NAME,"desc").send_keys("Bensin")

# #buat variabel tombol untuk eksekusi pencarian berdasarkan find_element(button Login)
buttonsubmitwithdraw=driver.find_element(By.NAME,"AccSubmit")

# #jalankan variabel tombol dengan fungsi click()
buttonsubmitwithdraw.click()