from flask import Flask
import urllib.request
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Welcome to my stock app! Add a symbol to the end of the URL to look it up.<h1>'

@app.route('/<symbol>')
def lookup_stock(symbol):
    info_json = urllib.request.urlopen(f"https://api.iextrading.com/1.0/stock/{symbol}/quote").read()
    info = json.loads(info_json)
    name = info['companyName']
    price = info['latestPrice']
    return f'<h1>{name} --> ${price}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)