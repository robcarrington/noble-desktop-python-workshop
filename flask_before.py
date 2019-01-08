from flask import Flask
# Add the following line: import urllib.request
# Add the following line: import json

app = Flask(__name__)

# Copy this block of code to create a new route
@app.route('/')
def hello():
    return '<h1>Welcome to my stock market app!</h1>'

# Paste your new route here
# Modify the route in the decorator. Change '/' to '/<symbol>'
# Rename your function and add the symbol parameter (e.g. "get_info(symbol)")

# Now you can use the symbol variable to call the API and store the json_data
# json_data = urllib.request.urlopen(f"https://api.iextrading.com/1.0/stock/{symbol}/book").read()

# load the json string into a dictionary: data = json.loads(json_data)
# grab the stock name: data['companyName']
# grab the stock price: data['latestPrice']
# return the name and price in an f-string!

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)