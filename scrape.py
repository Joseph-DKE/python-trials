from selenium import webdriver
import time
        
#path = r'C:\\Users\\Joseph Etse\\Desktop\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome('path to chromedriver')

browser.get('website link')

#browser.find_element_by_id('search_term').send_keys('.')
#browser.find_elements_by_class_name("payouts.ng-star-inserted")

#from register page click login
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div').click()

#from loogin page fill form
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[1]/input').send_keys('username/number')
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[3]/input').send_keys('password')

#click login
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/button').click()
'''
time.sleep(60)

frame_ref = browser.find_elements_by_tag_name("iframe")[0]
iframe = browser.switch_to.frame(frame_ref)
frame_ref = browser.find_elements_by_tag_name("iframe")[0]
iframe = browser.switch_to.frame(frame_ref)

time.sleep(1)
#autobutton
browser.find_element_by_xpath('/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/app-navigation-switcher/div/button[2]').click()
time.sleep(1)
#autocashout
browser.find_element_by_xpath('/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[2]/div[2]/div[1]/app-ui-switcher/div').click()
time.sleep(1)
#betamount
browser.find_element_by_xpath('/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[1]/div[1]/app-spinner/div/div[1]/input').send_keys('1')
time.sleep(1)
#betbutton
browser.find_element_by_xpath('/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[1]/div[2]/button/label').click()
'''

'''
time.sleep(1)
results = browser.find_elements_by_css_selector('app-payout-item div')
time.sleep(1)
#print(results)
resultData = [result.text for result in results]
print(resultData)

fin = ""
for i in resultData:
    fin += i + '\n'
with open("C:\\Users\\Joseph Etse\\Desktop\\aviatorDataset\\dataset.txt", 'a') as f1:
    f1.write(fin)
f1.close()
'''
'''
counter = 0
while True:
    time.sleep(60)
    frame_ref = browser.find_elements_by_tag_name("iframe")[0]
    iframe = browser.switch_to.frame(frame_ref)
    frame_ref = browser.find_elements_by_tag_name("iframe")[0]
    iframe = browser.switch_to.frame(frame_ref)
    results = browser.find_elements_by_css_selector('app-payout-item div')
    resultData = [result.text for result in results]
    if resultData[-1] is None:
        print(resultData)
        continue
    else:
        with open("C:\\Users\\Joseph Etse\\Desktop\\aviatorDataset\\dataset" + str(counter) + ".txt", 'w') as f1:
            f1.write(i for i in resultData + "\n")
        f1.close()
        counter += 1 
        break
'''