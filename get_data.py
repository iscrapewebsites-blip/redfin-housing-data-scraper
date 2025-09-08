from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


url = 'https://www.redfin.com/city/16409/CA/Sacramento'
driver.get(url)

### Test before directly running online Scraper ###


     
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

xnp = '//button[@aria-label="next"]'
count = 0
nextbtn = ''
while True:
     count += 1
     print(count)
     ## Get Data you want
     xp =  '//div[contains(@class,"HomeCardContainer")]'
     try:
          elements = driver.find_elements(By.XPATH, xp) # if you cannot fetch elements then code under it will be discarded

          for i, el in enumerate(elements):
               item = el.get_attribute('outerHTML')
               item = str(item)
               with open(f'data/elem_{count}_{i}.html', 'w', encoding='utf-8') as f:
                    f.write(item)
     except:
          print("error in fetching elements")
     
     ## Get Button to Next Page
     try:
          nextbtn = WebDriverWait(driver, 10).until(
               EC.visibility_of_element_located((By.XPATH, xnp))
          )
     except:
          print("next button not found!")
          break

     ## if next button is Hidden (last page)
     if "PageArrow--hidden" in nextbtn.get_attribute("class"):
          print("No more pages")
          break
     else:
          nextbtn.click()
          WebDriverWait(driver, 10).until(
                EC.invisibility_of_element((By.XPATH, '//div[@class="loading-spinner"]'))
            )
          time.sleep(1)

driver.quit()


