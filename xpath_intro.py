from lxml import html

# Let's grab the simple page source.
simple_page = open('data/simple.html').read()

# Let's open it with LXML so we can play around with xpath.
simple_tree = html.document_fromstring(simple_page)

