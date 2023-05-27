from forex_python.converter import CurrencyRates, CurrencyCodes

c=CurrencyRates()
def getCur(cur1,cur2,amount):
    try: 
        c.get_rates(cur1)
    except:
        return [False, "first currency type does not exist"]
    
    try:
        c.get_rates(cur2)
    except:
        return [False, "second currency type does not exist"]
    
    try: 
        return [True, f'{CurrencyCodes().get_symbol(cur2)}{round(c.get_rate(cur1, cur2) * float(amount),2)}']
    except:
        return [False, f"amount not a valid number"]
    

"""
>>>getCur(USD,USD,25)
$25
"""