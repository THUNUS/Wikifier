#coding: utf-8
'''
Created on 2015.7.25

@author: RyuLee
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from courseInfo.models import courseVideo
import time
import structure as st
import courseInfo
import re


def analyse(post): 
    struct = st.struct()
    struct.title = str()
    driver = webdriver.PhantomJS("\\utilities\\phantomJS\\bin\\phantomjs.exe")
    site = "https://class.coursera.org/"+post+"/lecture"
    print site
    driver.get(site)
    body = driver.find_element_by_tag_name("body")
    #print body.get_attribute("outerHTML")
    try:
        WebDriverWait(driver,5).until(
                                      EC.presence_of_element_located((By.TAG_NAME,"form")))
        form = driver.find_element_by_class_name("c-user-modal-content").find_element_by_tag_name("form")
        email = form.find_element_by_xpath("//input[@tabindex='10015']")
        email.send_keys("wing.nus@gmail.com")
        
        pwd = form.find_element_by_xpath("//input[@tabindex='10016']")
        pwd.send_keys("vM4HzTcN")
        button = form.find_element_by_xpath("//button[@tabindex='10018']")
        button.click()
    except Exception:
        print 'error in login'
        
    try:    
        WebDriverWait(driver,6).until(
                                      EC.presence_of_all_elements_located((By.XPATH,"//a[@class=\"lecture-link\"]")))
        #elem = driver.find_elements_by_xpath("//ul[@class='course-item-list-section-list']")
        time.sleep(1)
        #archs = driver.find_elements_by_xpath("//a[@class=\"lecture-link\"]")
        #read the navibar info from html_element
        while True:
            archs = driver.find_elements_by_xpath("//a[@class=\"lecture-link\"]")
            i = 0
            j = 0
            for arch in archs:
                print arch.get_attribute("textContent")
                if len(arch.get_attribute("textContent")) == 0:
                    j+=1
                if j >= 5:
                    time.sleep(1)
                    break
                i+=1
            if i < len(archs)-1:
                continue
            else:
                break    
        prettyName = prettyInfo(archs)
        for i,item in enumerate(archs):
            if prettyName[i]!= '':
                course = courseVideo(
                                     courseName = post,
                                     videoName = prettyName[i],
                                     resource_link = item.get_attribute("href")
                                     )
                course.save()
                print course.videoName
                print course.resource_link
            '''    navibar = st.navibar()
            if item.text.encode('utf-8')!='':
                a = item.find_element_by_tag_name("a")
                navibar.name = a.text.encode("utf-8")
                navibar.href = a.get_attribute("href").encode('utf-8')
                struct.skeleton.append(navibar)
                '''
         
        
        ''' 
        with open("D:\\java\\workplace\\demo\\temp\\struc.tmp",'w+') as temp:
            for i,section in enumerate(sections):
                refs = nodes[i].find_elements_by_tag_name("li")
                for ref in refs:
                    #list(nodesRef[section.get_attribute("innerHTML")]).append(ref.find_element_by_tag_name("a").get_attribute("innerHTML"))
                    str = ref.find_element_by_tag_name("a").get_attribute("innerHTML").encode("ascii")[1:ref.find_element_by_tag_name("a").get_attribute("innerHTML").index("(")]
                    code = ref.find_element_by_tag_name("a").get_attribute("data-lecture-id").encode("ascii")
                    temp.write(str+" +"+code+"\n")
                    print (str+" "+code)
            temp.close()
        '''
    except Exception:
        print 'error in locating'
    driver.quit()
    
def prettyInfo(archs):
    names = []
    for item in archs:
        try:
            groups = item.get_attribute("textContent").encode("utf-8").split(" ")
        except Exception:
            groups = item.get_attribute("textContent").encode("ascii").split(" ")
        names.append(groups)
    invalidSet = ('lecture','module','part','video','–','\n','\t','\r','\\n','-','.')
    invalidPattern = re.compile("(\d*\.\d*)|(\d*:\d*)|(\d*-\d*)",re.IGNORECASE)
    for i in range(len(names)):
        for j in range(len(names[i])):
            try:
                if str(names[i][j]).strip(" \t\n\r-").lower() in invalidSet or invalidPattern.match(str(names[i][j]).strip(" \t\n\r-")):
                    print names[i][j]
                    names[i][j] = ''
                    if str(names[i][j+1])[0].isdigit():
                        names[i][j+1] = ''
                elif names[i][j][0] == '(':
                    names[i][j] = ''
                    if names[i][j+1][-1] == ')':
                        names[i][j+1] = ''
            except Exception:
                continue
    prettyName = []
    for groups in names:
        prettyWord = " "
        prettyWord = prettyWord.join(groups)
        prettyName.append(prettyWord.lstrip(' -.:\n').rstrip())
    return prettyName
"""file = open("G:\\workplace\\git\\moocwiki\\metadata\\courselist.txt")
i = 0
for courseName in file:
    i += 1
    print i 
    print courseName
    analyse(courseName.rstrip())
 """   
#courseVideo.objects.all()
analyse('3d-motion')    