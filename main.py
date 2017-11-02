import random
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
all_quotes = BeautifulSoup(response)

quotes_file = open("quotes.csv", "w")
quotes_file.write("My dear ... just for you: \n\n")

print "My dear ... just for you: \n"

quotes = all_quotes.findAll("p", attrs={"class": "quoteContent"})

q = 1

for q in random.sample(quotes, 5):
    qu = q.string.lstrip(' ')
    print qu
    quotes_file.write(qu + "\n")
 
quotes_file.close() 




