import urllib2
import json
url='https://api.openaq.org/v1/latest';



resp=urllib2.urlopen(url);

html=resp.read();

data=json.loads(html)["results"]
c1=raw_input("first city:");
a=0;
while a==0:

    for i in data:
        if i["city"]==c1:

            a=1;

    if a==0:
        print "Not available city"
        c1=raw_input("first city:");
c2=raw_input("Second city:");
a=0;
while a==0:

    for i in data:
        if i["city"]==c2:

            a=1;

    if a==0:
        print "Not available city"
        c2=raw_input("Second city:");

for i in data:
    if i["city"]==c1:
        m1=i["measurements"];
for i in data:
    if i["city"]==c2:
        m2=i["measurements"]
print " "
print c1+" : "
print m1[0]["parameter"]
print m1[0]["value"]
print m1[0]["unit"]
print "  "
print c2+" : "
print m2[0]["parameter"]
print m2[0]["value"]
print m2[0]["unit"]
