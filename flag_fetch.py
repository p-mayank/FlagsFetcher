from bs4 import BeautifulSoup
import os
import requests
import urllib.request
import urllib

def crawler():
    url="https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('a', {'class':'image'}):
        href=link.get('href')
        nm=link.get('title')
        name=nm[9:]
        link = ("https://www.wikipedia.org"+(href))
        crawl2(link, name)
        
def crawl2(link, name):
	url=link
	source_code=requests.get(url)
	text = source_code.text
	soup = BeautifulSoup(text, 'html.parser')
	tag =soup.body
	count=0
	for link in tag.findAll('a', {'class':None}):
		count+=1
		k=link.get('href')
		if(count>1 and k is not None):
			if(k.count('//upload.wikimedia.org/wikipedia/commons')==1):
				href=link.get('href')
				link = ("https:"+(href))
				get_image(url, name)
				break

def get_image(url, name):
    filename = name + ".svg"
    urllib.request.urlretrieve(url, filename)
    print(name)


crawler()