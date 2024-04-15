from __future__ import annotations

import pendulum

import yfinance as yf
import pandas as pd
import time
from airflow.macros import ds_add
from airflow.decorators import task, dag

from pathlib import Path

from datetime import datetime, timedelta


from confluent_kafka import Producer

def send_to_kafka(topic, data):
    try:
        conf = {'bootstrap.servers': 'kafka:29092',
                'message.timeout.ms': 5000}  # Endereço do broker Kafka

        # Cria o produtor Kafka
        p = Producer(**conf)

        # Callback para lidar com a entrega das mensagens
        def delivery_report(err, msg):
            if err is not None:
                print(f'Erro ao enviar mensagem para o tópico {msg.topic()}: {err}')
            else:
                print(f'Mensagem enviada com sucesso para o tópico {msg.topic()}')

        p.produce(topic, data.encode('utf-8'), callback=delivery_report)
        p.flush()
        p.close()
    except:
        print(f'Erro ao enviar mensagem para o tópico {topic}')


TICKERS = ['ADA-USD','MATIC-USD','BNB-USD', 'USDT-USD', 'LEO-USD', 'OP-USD', 'BTC-USD', 'ETH-USD', 'DOGE-USD', 'SOL-USD']
    
@task()
def get_history(ticker,ds=None, ds_nodash=None):
    file_path = f"./data/{ticker}/{ticker}_{ds_nodash}.csv"
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    df = yf.Ticker(ticker).history(
        period = "1d",
        interval = "15m",
        start = ds_add(ds, -1),
        end = ds,
        prepost = "True"
    )
    df['ticker'] = ticker
    df.to_csv(file_path, index=True)
    
    df['data'] = pd.to_datetime(df.index, unit='s').strftime('%Y-%m-%d %H:%M')
    
    df_json = df.to_json(orient="records")
    send_to_kafka("CRYPTO_CURRENCY", df_json)

@dag(
  schedule_interval = "@daily",
  start_date=datetime.now() - timedelta(days=30),
  catchup = False
)

def get_crypto_dag():
  for ticker in TICKERS:
    get_history.override(task_id=ticker)(ticker)

dag = get_crypto_dag()
    