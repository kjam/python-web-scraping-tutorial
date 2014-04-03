import urllib2
from email.MIMEText import MIMEText
import smtplib
from bs4 import BeautifulSoup

GMAIL_LOGIN = 'pyladiestest@gmail.com'
GMAIL_PASSWORD = 'YOU NO CAN HAZ'


def send_email(subject, message, from_addr=GMAIL_LOGIN, to_addr=GMAIL_LOGIN):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Reply-To'] = 'happyhours@noreply.com'

    server = smtplib.SMTP('smtp.gmail.com', 587)  # port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(GMAIL_LOGIN, GMAIL_PASSWORD)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.close()


def get_site_html(url):
    source = urllib2.urlopen(url).read()
    return source


def get_tree(url):
    source = get_site_html(url)
    tree = BeautifulSoup(source)
    return tree


if __name__ == '__main__':

    stuff_i_like = ['burger', 'wine', 'sushi', 'sweet potato fries', 'BBQ']
    found_happy_hours = []
    my_happy_hours = []

    # First, I'm going to identify the areas of the page I want to look at
    tables = get_tree(
        'http://www.downtownla.com/3_10_happyHours.asp?action=ALL')

    # Then, I'm going to sort out the *exact* parts of the page
    # that match what I'm looking for...
    for t in tables.findAll('p', {'class': 'calendar_EventTitle'}):
        text = t.text
        for s in t.findNextSiblings():
            text += '\n' + s.text
        found_happy_hours.append(text)

    print "The scraper found %d happy hours!" % len(found_happy_hours)

    # Now I'm going to loop through the food I like
    # and see if any of the happy hour descriptions match
    for food in stuff_i_like:
        for hh in found_happy_hours:
            # checking for text AND making sure I don't have duplicates
            if food in hh and hh not in my_happy_hours:
                print "YAY! I found some %s!" % food
                my_happy_hours.append(hh)

    print "I think you might like %d of them, yipeeeee!" % len(my_happy_hours)

    # Now, let's make a mail message we can read:
    message = 'Hey Katharine,\n\n\n'
    message += 'OMG, I found some stuff for you in Downtown, take a look.\n\n'
    message += '==============================\n'.join(my_happy_hours)
    message = message.encode('utf-8')
    # To read more about encoding:
    # http://diveintopython.org/xml_processing/unicode.html
    message = message.replace('\t', '').replace('\r', '')
    message += '\n\nXOXO,\n Your Py Script'

    # And email it to ourselves!
    email = 'katharine@pyladies.com'
    send_email('Happy Hour Update', message, from_addr=GMAIL_LOGIN,
               to_addr=email)
