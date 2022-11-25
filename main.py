import pandas as pd
import flask
from flask import Flask, request, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

Credentials = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\diego\OneDrive\Desktop\aaaa\claves.json", scope)
cliente = gspread.authorize(Credentials)

sheet = cliente.open("Estacionamientos Database").sheet1
x = sheet.acell("A1").value
x= str(x)
print(x)


app = Flask(__name__)    
app.static_folder = 'static'

@app.route('/')
def inicio():
    return render_template("/index.html", x=x)


if __name__ == '__main__':
    app.run(debug=True)




   