import requests
import pandas as pd
import time
import estado
import flask
from flask import Flask, request, render_template
app = Flask(__name__)    
app.static_folder = 'static'

@app.route('/')
def inicio():
    from estado import x
    return render_template("index.html",x=x)


if __name__ == '__main__':
    app.run(debug=True)




   