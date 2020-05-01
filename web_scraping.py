from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq


myurl = 'https://www.bestbuy.com/site/arlo-pro-3-6-camera-indoor-outdoor-wire-free-2k-hdr-security-camera-system-white/6364585.p?skuId=6364585'
client = ureq(myurl)
page_html = client.read()
client.close()
for i in range(20): 
	sleep(3)  
	page_soup = soup(page_html,'html.parser')

	container  = page_soup.findAll('div',{'class':'price-box'})
# print(container[0])
# print(len(container))
	containers = container[0]
	print(containers)
# print(containers )
# price = containers.findAll('div',{'class': 'priceView-hero-price'})
# print(price[0].text)