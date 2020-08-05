import json
import requests
import re
import xml.etree.ElementTree as ET
from datetime import datetime


# import matplotlib.pyplot as plt
# import matplotlib.axes



def fetch(page_number, location_id):
    # def fetch():
    url = 'https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page=' + page_number
    respuesta = requests.get(url)
    respuesta2 = respuesta.json()
    a = respuesta2.get("data")
    datas = [{'Monto': x['amount'], 'User': x['userId']} for x in a if x.get('location').get('id') == location_id]
    #dataset = json.dumps(datas)
    return datas

    #c = [i for i in a if i.get('location').get('id') == location_id]
    #print(c)
    #print(c[0]['userId'], c[0]['amount'])

def transform(datas):
    #a2 = datas[2]['Monto']
    a2 = [{'Monto2': float(re.sub(r'[^\d\-.]', '', x['Monto'])), 'User2': x['User']} for x in datas]
    print(a2)

    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    datas = fetch(str(12), 8)
    df = transform(datas)
    #report(df)
