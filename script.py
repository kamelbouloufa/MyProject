import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# خيارات المتصفح
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")  # حل مؤقت لمشكلة GPU
driver = webdriver.Chrome(options=options)

print("🚀 تشغيل المتصفح...")
driver.get("http://bc.vc/l5w1mjE")
print("✅ تم فتح الرابط بنجاح!")

time.sleep(8)  # انتظار الصفحة للتحميل بالكامل

try:
    skip_button = driver.find_element(By.ID, "getLink")  # زر التخطي الصحيح
    skip_button.click()
    print("🎉 تم الضغط على زر التخطي!")
except:
    print("⚠️ لم يتم العثور على زر التخطي! تجربة الضغط على Enter...")
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

time.sleep(3)  # مهلة صغيرة قبل الإغلاق
driver.quit()
