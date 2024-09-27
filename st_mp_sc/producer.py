from confluent_kafka import Producer
import time
import requests
import json
import threading

headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
 'Content-Type': 'application/json',
 'Authorization': 'Bearer <token>'
}
producer = Producer({'bootstrap.servers': 'localhost:9092',
                    'client.id': 'stock-price-producer'})

def nasdaq_btm(stock):
    while True:
        try:
            url = 'https://query2.finance.yahoo.com/v8/finance/chart/btm-usd'
            response = requests.get(url, headers=headers)
            data = json.loads(response.text)
            price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
            producer.produce('nasdaq', key=None, value=json.dumps({'stock': stock, 'price': price}))
            producer.flush()
            print(f"Sent bytom {stock} price to Kafka: {price}")
        except Exception as e:
            print(f"Error fetching/sending stock price: {e}")


def nasdaq_dogecoin(stock):
    while True:
        try:
            url = 'https://query2.finance.yahoo.com/v8/finance/chart/doge-usd'
            response = requests.get(url, headers=headers)
            data = json.loads(response.text)
            price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
            producer.produce('nasdaq', key=None, value=json.dumps({'stock': stock, 'price': price}))
            producer.flush()
            print(f"Sent dogecoin {stock} price to Kafka: {price}")
        except Exception as e:
            print(f"Error fetching/sending stock price: {e}")

start = time.time()

btm_usd_thread = threading.Thread(target=nasdaq_btm, args=('BTM-USD',))
doge_usd_thread = threading.Thread(target=nasdaq_dogecoin, args=('DOGE-USD',))

btm_usd_thread.start()
doge_usd_thread.start()

btm_usd_thread.join()
doge_usd_thread.join()

end = time.time()
print('Execution Time: {}'.format(end-start))
