import json
from urllib import urlopen

ip_info = urlopen('http://freegeoip.net/json/').read()

my_ip = json.loads(ip_info)

print "I think you're at: %f lat, %f long and in %s" % (
    my_ip.get('latitude'), my_ip.get('longitude'), my_ip.get('city'))
