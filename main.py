# Python program automating a task that doesn't actually NEED to be automated. But I do it anyways.
# Made by: Nathaniel Masson // Nate // Naedrae // Razuul
# suggestions are always welcome.
# enjoy
# started: December 4th, 2022
# finished: January 22nd, 2023
# edited: January 29th, 2023
# edited means: adding a check function for every input receiver so I don't have to check it every time.
# mind you, I didn't go at this every day. Only on the occasional Sunday
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# ----------------------------------------------------------------------------------------------------------------------
# console input, assigning variables
title = input("What is the title of this Sunday?")
description = input("Notes Link?")
saveauto = input("Would you like to save automatically?")
title = "Kairos Church /// " + title
description = "Thanks for joining us online.  Be sure to share, invite or start a watch part. " \
              "You can also watch online at www.youtube.com/kairoschurch\nFill Out Your Connect" \
              " Card  +++ www.kairos.church/connect-card\nShare a Prayer or Praise +++  www.k" \
              "airos.church/prayer-praise\nNotes +++ " + description + "\nMaking a decision to " \
              "follow Jesus +++ www.kairos.church/follow-jesus\nDownload our App +++ https://" \
              "tithely.app.link/kairos-church\n"
path = './chromedriver.exe'
browser = webdriver.Chrome(path)
error = "A known error occured. This happend because the device running this\nprogram operated too slowly.\n\nRerunning the program should fix this error."

# ----------------------------------------------------------------------------------------------------------------------
# launch chrome, go to resi, input user and pass, and click login.
browser.get('https://studio.resi.io/settings/destination-groups?refresh')
time.sleep(1)
browser.find_element('name', 'username').send_keys('username')
browser.find_element('name', 'password').send_keys('password')
browser.find_element('id', 'button---1').click()
time.sleep(2)


# ----------------------------------------------------------------------------------------------------------------------
# beyond this point, cookies must be saved from previous 'browser.get' function.
# Goes to the editing title/desc portion of the destination group
try:
    browser.get('https://studio.resi.io/settings/destination-groups/76c60c45-d334-42fd-8087-a6f479ba1880')
    time.sleep(2)

    browser.find_element(By.CLASS_NAME, 'css-1ctyr6v-rui-button-base__container-rui-icon-button__container').click()
    time.sleep(2)
except:
    print(error)
    time.sleep(10)
    exit()

list = ['placeholder', 'name', 'yt.title', 'yt.description', 'fb.title', 'fb.description'] # <------ allows for for loops instead of writing every bit out.
# ----------------------------------------------------------------------------------------------------------------------
# created a function here for minimizing of code; leisure purposes
# Does the last bit of what it's designed to do. You can figure that out xDD
def main():
    for i in range(1, 6):
        if 'description' in list[i]:
            try:
                browser.find_element(By.ID, list[i]).send_keys(Keys.CONTROL + "a")
                browser.find_element(By.ID, list[i]).send_keys(Keys.DELETE)
                browser.find_element(By.ID, list[i]).send_keys(description)
                continue
            except:
                print(error)
                time.sleep(5)
                exit()
        try:
            browser.find_element(By.ID, list[i]).send_keys(Keys.CONTROL + "a")
            browser.find_element(By.ID, list[i]).send_keys(Keys.DELETE)
            browser.find_element(By.ID, list[i]).send_keys(title)
            continue
        except:
            print(error)
            time.sleep(5)
            exit()

main()
#-----------------------------------------------------------------------------------------------------------------------
# obviously, this checks the automatically inputted text, then clicks save :)
def check():
    variable = ['placeholder']
    for i in range(1, 6):
        variable.append(browser.find_element(By.ID, list[i]).get_attribute("value"))
    for i in range(1, 6):
        if list[i] == 'name':
            if variable[i] == title:
                print('name: passed')
                continue
            else:
                print("something weird happend.. exiting to prevent extraneous issues.")
                print('name: error')
                exit()
        if 'description' in list[i]:
            if variable[i] == description:
                print('description: passed')
                continue
            else:
                print("something weird happend.. exiting to prevent extraneous issues.")
                print('description: error')
                exit()
        if 'title' in list[i]:
            print(list[i])
            print(variable[i])
            if variable[i] in title:
                print('title: passed')
                continue
            else:
                print("something weird happend.. exiting to prevent extraneous issues.")
                print('title: error')
                exit()
    print('Congratulations! It worked properly!!')
    time.sleep(4)
    # clicks save. (don't enable unless you want it to save automatically)
    if 'yes' in saveauto:
        browser.find_element(By.CLASS_NAME, 'css-sq47s1-rui-button-base__container-rui-button__container').click()
    time.sleep(1)
    exit()
#-----------------------------------------------------------------------------------------------------------------------


check()
