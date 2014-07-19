from bs4 import BeautifulSoup
import urllib2

url="http://www.fpm.iastate.edu/utilities/plantdata/history_data.asp?tagname=Total+MWatts&date=2014-07-17"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

table = soup.find('table')

rows = table.findAll('tr')

for tr in rows:
  cols = tr.findAll('td')
  for td in cols:
     text = ''.join(td.find(text=True))
     if "/" not in text:
     	print text.replace(":", " ") + " ",
   
  print 