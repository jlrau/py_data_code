import urllib.request
import xml.etree.ElementTree as etree
import csv

urllib.request.ProxyHandler()
page = urllib.request.urlopen('https://www.w3schools.com/xml/cd_catalog.xml')
xml_content = page.read()
e = etree.fromstring(xml_content)

cd_data = open('cd_data.csv', 'w')
csvwriter = csv.writer(cd_data)
cd_head = []

count = 0
for member in e.findall('CD'):
    cd = []
    if count == 0:
        for c in member:
            cd_head.append(c.tag)
        csvwriter.writerow(cd_head)
        count = count + 1    
    
    for c in member:
        cd.append(c.text)
    csvwriter.writerow(cd)
    
cd_data.close()
