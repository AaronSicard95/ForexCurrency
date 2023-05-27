from flask import Flask, render_template, request,flash
from forex_python.converter import CurrencyRates
from currency import *

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def loadHome():
    return render_template('default.html', cur1 = "", cur2 = "", amount = "")

@app.route('/result', methods=['POST'])
def loadResult():
    data = request.form
    result = getCur(data['cur1'],data['cur2'],data['amount'])
    if result[0] == False:
        flash(result[1])
        return render_template('default.html', cur1 = data['cur1'], cur2 = data['cur2'], amount = data['amount'])
    else:
        return render_template('results.html', newAmount = result[1])