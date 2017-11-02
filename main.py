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

for quote in range(5):
    print random.choice(quotes).string.lstrip(' ')
    quotes_file.write(random.choice(quotes).string.lstrip(' ') + "\n") #izpis je drugacen kot v csv datoteki
                                                                        #razumem zakaj, nvm pa resitve
quotes_file.close()                                                     #zgleda pa, da se quotes ne ponavljajo

'''with open("quotes.txt", "w+") as quotes_file:
    quotes_file.write("My dear ... just for you: \n\n")
    for quote in range(5):
        quote = str(random.choice(quotes).string.lstrip(' ')) # ozadje quote se tukaj obarva rumeno + izpis je drugacen kot v txt.datoteki
        quotes_file.write(quote + "\n")'''
