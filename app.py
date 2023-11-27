import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder = "templates")

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        currency = request.form.get('currency')
        amount = request.form.get('amount')
        amount = float(amount)

        response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
        data = response.json()
        rates = data[0]['rates']

        rates_dict = {}

        for rate in rates:
            code = rate['code']
            rates_dict[code] = {'currency': rate['currency'], 'bid': rate['bid'], 'ask': rate['ask']}
        
        if currency in rates_dict.keys():
            cost = round(amount * float(rates_dict[currency]['ask']), 2)

            return render_template("result.html", currency = currency, amount = amount, cost = cost)
    
    return render_template("home.html")

if __name__ == 'main':
    app.run(debug = True)
   


