import requests

while True:

    try:
        print("\nInput the initial currency (JPY, CNY, USD, BRL, EUR): ")
        i = input()
        if len(i) == 0:
            raise Exception
        print("\nInput the final currency (JPY, CNY, USD, BRL, EUR): ")
        f = input()
        if len(i) == 0:
            raise Exception
        resp = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=" + i +
                            "&to_currency=" + f + "&apikey=PVBPVPCWNSVP7I5J").json()
        print("1 " + i.upper() + " worth " + resp['Realtime Currency Exchange Rate']['5. Exchange Rate'] + " " + f.upper())
        dados = open("dados.csv", "w+")
        writee = i+"," + resp['Realtime Currency Exchange Rate']['5. Exchange Rate']+ "," +f
        dados.write(writee)
        dados.close()
        print("\nYour file (.CSV) has been saved, with currencies and exchange rate.")
    except:
        print("Enter valid currencies:")
