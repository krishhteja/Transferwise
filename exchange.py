import requests, json, time
from twilio.rest import Client

token = "TRANSFERWISE TOKEN"  
url = "https://api.transferwise.com/v1/rates?source=EUR&target=INR" #From euro to indian rupee : SOURCE - source currency (eur), target - target currency (inr)
headers = {'Authorization':'Bearer TRANSFERWISE_KEY'}

def getExchange():
    r = requests.get(url=url, headers=headers) 
    data = r.json()
    exchange = data[0]['rate']
    if exchange > 79: #EXCHANGE AMOUNT TO CHECK
        twilio = "TWILIO KEY"
        pwd = "TWILIO PASSWORD"
        number = "TWILIO PHONE"
        client = Client(twilio, pwd)

        message = client.messages.create(
                             body="Time to transfer. Current rate is {}".format(exchange) ,
                             from_=number,
                             to='YOUR NUMBER'
                         )
    else:
        print("Exchange value not good at {}".format(exchange))
        
while True:
    getExchange()
    time.sleep(1800)