from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options

#replace the string to the location of chromedriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365')

try:
    element = driver.find_element_by_partial_link_text("See all reviews")
except Exception:
    time.sleep(10)
    element = driver.find_element_by_partial_link_text("See all reviews")

actions = ActionChains(driver)
actions.move_to_element(element).perform()

try: 
    element.click()
except Exception:
    time.sleep(5)
    element = driver.find_element_by_partial_link_text("See all reviews")
    element.click()

try:
    selectaria = driver.find_element_by_xpath("//*[contains(@aria-label,'Sort by')]/option[@value='submission-desc']").click()
except Exception:
    time.sleep(5)
    selectaria = driver.find_element_by_xpath("//*[contains(@aria-label,'Sort by')]/option[@value='submission-desc']").click()

ratinglist = list()
flag = 1
reviews = driver.find_elements_by_css_selector('.review')
while(flag): 
    for review in reviews:
        starno = review.find_element_by_css_selector("span.visuallyhidden.seo-avg-rating").text
        date = review.find_element_by_css_selector('.review-date-submissionTime').text
        try:
            title = review.find_element_by_css_selector('.review-title').text
        except Exception:
            title = 'No title'
        reviewtext = review.find_element_by_css_selector('.review-description').text.replace('\n', '  ')
        name = review.find_element_by_css_selector('.review-footer-userNickname').text
        if ('December' in date):
            flag = 0
            break
        else:
            ratinglist.append([starno,date,title,reviewtext,name])
    try:
        driver.find_element_by_css_selector('button.paginator-btn.paginator-btn-next').click()
    except Exception:
        time.sleep(20)
        driver.find_element_by_css_selector('button.paginator-btn.paginator-btn-next').click()

df = pd.DataFrame(ratinglist)

ds = df.to_csv('dataset.csv', index=False)
#print(ratinglist)

time.sleep(5)
driver.quit()

