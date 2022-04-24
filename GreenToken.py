from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())


#Goes to green Token site

def fillin(driver):
    iunderstand = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[3]/div/div[5]/span/label')
    iunderstand.click()
    driver.switch_to.default_content()

    wait()

    feverc = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[1]/div/div[2]/span[2]/label')
    feverc.click()

    COUGH = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[3]/div/div[2]/span[2]/label')
    COUGH.click()

    soreT= driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[5]/div/div[2]/span[2]/label')
    soreT.click()

    shortB =  driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[7]/div/div[2]/span[2]/label')
    shortB.click()

    changes = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[9]/div/div[2]/span[2]/label')
    changes.click()

    changesell = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[11]/div/div[2]/span[2]/label')
    changesell.click()

    head = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[13]/div/div[2]/span[2]/label')
    head.click()

    fatigue = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[15]/div/div[2]/span[2]/label')
    fatigue.click()

    closec = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[9]/div/div[1]/div/div[2]/span[2]/label')
    closec.click()

    trav = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[9]/div/div[3]/div/div[2]/span[2]/label')
    trav.click()

    test = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[9]/div/div[5]/div/div[2]/span[2]/label')
    test.click()


    lastsubmit = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[11]/div')
    lastsubmit.click()
    wait()
    driver.close()

def wait():
    time.sleep(10)
    

def login(Username,passw,driver):
    driver.get('https://workflow7prd.nwu.ac.za/covid-screening/?locale=en_ZA')
    
    wait()
    
    #Receives Username
    user = driver.find_element_by_xpath('/html/body/div/div/div[1]/form/section[1]/input')
    user.send_keys(Username)
    
    #Receives password
    password = driver.find_element_by_xpath('/html/body/div/div/div[1]/form/section[2]/input')
    password.send_keys(passw)
    
    #Enter
    SUBMITBUTTON = driver.find_element_by_xpath('/html/body/div/div/div[1]/form/section[4]/input[4]')
    SUBMITBUTTON.click()
    wait()
    fillin(driver)
    #driver.close()
    

def UserPass():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    usernames = [""]
    passwords = [""]

    for i in range(0, len(usernames)):
        login(usernames[i], passwords[i], driver)
        
UserPass()