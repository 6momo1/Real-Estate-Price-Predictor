from bs4 import BeautifulSoup
from collections import OrderedDict
import json


def get_info(source_code):
    # this function returns a dictionary about a real estate home information
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

    return json.dumps(OrderedDict(table_data))

# html = 'html.txt'        
# print(get_info(html))


