'''
import requests
import pandas as pd
import time
def wifi():
    while True:
        url = 'http://192.168.100.174/'
        html = requests.get(url).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        print(df)
        df.to_csv('/Users/matiasmullerlanas/Downloads/codigoAdruino/output.csv', header=True, index=False)
        df1= pd.read_csv('/Users/matiasmullerlanas/Downloads/codigoAdruino/output.csv')
        x=df1.iloc[0,0]
        if x==1:
            print('verde')
        else:
            pass
        
        time.sleep(3)
        return x
    
'''
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import requests
import time

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

Credentials = ServiceAccountCredentials.from_json_keyfile_name("/Users/matiasmullerlanas/Downloads/aaaa/claves.json",)
cliente = gspread.authorize(Credentials)

#sheet = client.create("Estacionamientos Database")

#sheet.share("diego.gdoydiaz@gmail.com", perm_type="user", role="writer")



while True:
    url = 'http://192.168.100.174/'
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    data = df.to_csv('/Users/matiasmullerlanas/Downloads/aaaa/output.csv', header=True, index=False)
    df1=pd.read_csv('/Users/matiasmullerlanas/Downloads/aaaa/output.csv')
    x = df1.iloc[0,0]
    print(x)
    x= str(x)
    
    sheet = cliente.open("Estacionamientos Database").sheet1
    sheet.update_cell(1, 1, x)


