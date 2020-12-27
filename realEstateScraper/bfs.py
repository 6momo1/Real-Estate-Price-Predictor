from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import csv



def write_to_csv(data):

    string = ''
    li = []
    for (k,v) in data.items():
        li.append(v)

    with open('house_data_test2.csv', mode='a',newline='') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(li)



def get_info(source_code):
    # returns a dictionary then writes

    soup = BeautifulSoup(source_code, 'html.parser')

    table_data = []

    address = soup.findAll("div", {"class": "propertyheader-address"})
    table_data.append(['address',address[0].text])

    price = soup.findAll("div", {"class": "propertyheader-price"})
    table_data.append(['price',price[0].text])

    for row in soup.findAll('tr'):
        elements = row.text.strip('\n').split('\n')
        for elem in elements:
            if elem == '':
                elements.remove('')
        table_data.append(elements)

    data = OrderedDict(table_data)

    write_to_csv(data)




