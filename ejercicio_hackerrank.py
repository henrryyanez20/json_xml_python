import json
import requests
import xml.etree.ElementTree as ET
from datetime import datetime


# import matplotlib.pyplot as plt
# import matplotlib.axes



def fetch(page_number, location_id):
    # def fetch():
    url = 'https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page=' + page_number
    respuesta = requests.get(url)
    dataset = respuesta.json()
    a = dataset.get("data")
    filtro = [{'User': x['userId'], 'Monto': x['amount']} for x in a if x.get('location').get('id') == location_id]
    print(filtro)

    #c = [i for i in a if i.get('location').get('id') == location_id]
    #print(c)
    #print(c[0]['userId'], c[0]['amount'])

    # b = json.dumps(c, indent=4)
    # print(b)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fetch(str(7), 8)
