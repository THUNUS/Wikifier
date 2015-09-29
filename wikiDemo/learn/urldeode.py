from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
def decode(dict):
    
    terms = int(dict['section'][0]);
    chapter = int(dict['section'][1]);
    print os.path.abspath(os.curdir)
    driver = webdriver.PhantomJS("phantomjs.exe")
    #driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    site_url = "https://class.coursera.org/"+dict['course']+"/lecture"
    print site_url
    driver.get(site_url)
    en_code = ""
    try:
        WebDriverWait(driver,10).until(
                                      EC.presence_of_element_located((By.XPATH,"//div[@data-js='login-body']")))
        
        WebDriverWait(driver,10).until(
                                      EC.presence_of_element_located((By.XPATH,"//div[@data-js='login-body']")))
        
        form = driver.find_element_by_xpath("//div[@data-js='login-body']").find_element_by_class_name("c-user-modal-content").find_element_by_tag_name("form")
        print "find"
        #print form.get_attribute("innerHTML")
        email = form.find_element_by_xpath("//input[@tabindex='10013']")
        email.send_keys("wing.nus@gmail.com")
        print "find email"
        pwd = form.find_element_by_xpath("//input[@tabindex='10014']")
        pwd.send_keys("csiscdtlLIFT-15")
        print "find password"
        button = form.find_element_by_xpath("//button[@tabindex='10016']")
        button.click()
        try:
            WebDriverWait(driver,10).until(
                                          EC.presence_of_all_elements_located((By.XPATH,"//div[@class='coursera-page']")))
            print "find page"
            elem = driver.find_elements_by_xpath("//ul[@class='course-item-list-section-list']")
            hrefs = elem[terms-1].find_elements_by_class_name('lecture-link')
            en_code = hrefs[chapter-1].get_attribute("data-lecture-id")
            print "en_code ="+en_code 
        except Exception:
            print "error in 2"
    except Exception:
        print "error in 1"
    finally:
        driver.close()
        return en_code
