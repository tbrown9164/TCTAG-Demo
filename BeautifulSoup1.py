import requests
import mechanize
from bs4 import BeautifulSoup
import http.cookiejar


import csv

#page = requests.get("https://web.archive.org/web/20161022120719/http://www.nga.gov/collection/anB1.htm")
#page=  requests.get("http://10.1.115.164/view_logged_data.html")
#page=   requests.get("http://10.1.115.164/index.html")

#page
#page.status_code
#page.content

#soup= BeautifulSoup(page.content, 'html.parser')

#print (soup.prettify())

cj = http.cookiejar.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("http://10.1.115.164/view_logged_data.html")

br.select_form(nr=0)
br.form['password'] = '1234'
br.submit()

print  (br.response().read())

#list(soup.children)
#last_links= soup.find(class_='AlphaNav')
#last_links.decompose()
#f = csv.writer(open('b1_artist_names.csv','w'))
#f.writerow(['Name','Link'])

#artist_name_list= soup.find(class_='BodyText')

#artist_name_list_items= artist_name_list.find_all('a')

#for artist_name in artist_name_list_items:
#    names = artist_name.contents[0]
#    links = 'https://web.archive.org' + artist_name.get('href')
    #print(artist_name.prettify())   when displaying the whole tag
    #print(names)
    #print(links)
    #f.writerow([names, links])


