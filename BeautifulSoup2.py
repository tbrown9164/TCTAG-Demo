import requests
import mechanize
import urllib3
from bs4 import BeautifulSoup
import http.cookiejar


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

with requests.Session() as s:

    p = s.post("http://quora.com", data={
        "email": '*****@gmail.com',
        "password": "******"
    })
    print("ptext printout", p.text)

    base_page = s.get('https://quora.com')
    soup = BeautifulSoup(base_page.content, 'html.parser')
    print("title:", soup.title)
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






