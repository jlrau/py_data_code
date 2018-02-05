import urllib.request
import xml.etree.ElementTree as etree
import csv

url = 'https://www.w3schools.com/xml/cd_catalog.xml'
source_element = 'CD'
target_file = 'xml_data.csv'

urllib.request.ProxyHandler()
page = urllib.request.urlopen(url)
xml_content = page.read()
e = etree.fromstring(xml_content)

xml_data = open(target_file, 'w')
csvwriter = csv.writer(xml_data)
xml_head = []

count = 0
for member in e.findall(source_element):
    xml_row = []
    if count == 0:
        for item in member:
            xml_head.append(item.tag)
        csvwriter.writerow(xml_head)
        count = count + 1
    
    for item in member:
        xml_row.append(item.text)
    csvwriter.writerow(xml_row)
    
xml_data.close()
