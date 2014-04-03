from bs4 import BeautifulSoup

# Let's grab the simple page source.
simple_page = open('data/simple.html').read()

# Let's open it with BS so we can iterate over the family tree.
simple_soup = BeautifulSoup(simple_page)

# Let's highlight our current element and return it so we can play around!
current_elem = simple_soup.findAll('div', {'class': 'navblock'})[1]
