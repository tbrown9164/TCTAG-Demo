import requests
import mechanize
import urllib3
from bs4 import BeautifulSoup
import http.cookiejar
from selenium import webdriver         #for selenium alternative to logging in
from selenium.webdriver.common.keys import Keys


import csv



#with requests.Session() as s:

#    p = s.post("http://10.1.115.164/", data={
#        "email": '*******',
#        "password": "1234"
#    })
#    print(p.text)

#    base_page = s.get('http://10.1.115.164/view_logged_data.html')
#    soup = BeautifulSoup(base_page.content, 'html.parser')
#    print(soup.title)

#with requests.Session() as s:

 #   p = s.post("http://quora.com", data={
 #       "email": '*****@gmail.com',
 #       "password": "******"
 #   })
 #   print("ptext printout", p.text)

#selenium alternative
url = "https://dev.mtsecho.com/login"
driver = webdriver.Firefox()
driver.get( url )

username = driver.find_element_by_id( 'loginEmail' )
username.send_keys( 'vm2@mtsecho.com' )
password = driver.find_element_by_id( 'loginPassword' )
password.send_keys( 'Vm2Vm2' )
password.send_keys( Keys.RETURN )

#we should be on this page now and able to scrape
page = requests.get("https://dev.mtsecho.com/")

page.status_code

soup= BeautifulSoup(page.content, 'html.parser')

#print (soup.prettify())             #if we just want a dump of the page


#base_page = s.get('https://quora.com')
#soup = BeautifulSoup(base_page.content, 'html.parser')
#print("title:", soup.title)
#print( soup.prettify() )
#print('first a tag', soup.a)
#a_list = soup.find( class_='BodyText' )
#a_list = soup.find(class_="body")
a_list= soup.find_all('a')

i=0
for item in a_list:
    print( 'a list ordinal',i,':', item )
    i=i+1
    # f.writerow([names, links])
print('done')






